import os, io
from pathlib import Path
import tempfile
from PIL import Image
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ruta = Path(__file__).resolve().parents[2] / "imagenes_prueba" / "prueba.png"

formatos = ["jpg", "jpeg", "png", "webp", "tiff", "tif", "gif", "bmp", "ico"]

def convertirImagen(imagen,formato): 
    
    if formato in ["jpg", "jpeg", "tiff", "tif", "bmp"]:
        if imagen.mode in ("RGBA", "LA") or (imagen.mode == "P" and "transparency" in imagen.info):
            fondo = Image.new("RGB", imagen.size, (255, 255, 255))
            fondo.paste(imagen, mask=imagen.split()[-1])
            imagen = fondo
        else:
            imagen = imagen.convert("RGB")
            
    elif formato in ["png", "webp", "ico"]:
        if imagen.mode not in ("RGB", "RGBA"):
            imagen = imagen.convert("RGBA")
            
    elif formato == "gif":
        imagen = imagen.convert("P")
    
    return imagen

def convertir_a_formato(ruta_imagen, ruta_salida, formato):
    try: 
        im = Image.open(ruta_imagen)
        im = convertirImagen(im, formato.lower())
        ruta_salida = Path(ruta_salida)
        im.save(ruta_salida, formato.upper())
    except:
        raise HTTPException(status_code=400, detail="Archivo no es una imagen válida")
    

@app.post("/convert")
async def convert_image(
    file: UploadFile = File(...),
    format: str = Form(...)
):

    # archivo temporal entrada
    temp_input = tempfile.NamedTemporaryFile(delete=False)
    contenido = await file.read()
    temp_input.write(contenido)
    temp_input.close()

    # archivo temporal salida
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=f".{format}")
    temp_output.close()

    # usar tu función de conversión
    convertir_a_formato(temp_input.name, temp_output.name, format)

    # leer archivo convertido
    with open(temp_output.name, "rb") as f:
        data = f.read()

    # limpiar archivos temporales
    os.remove(temp_input.name)
    os.remove(temp_output.name)

    return Response(
        content=data,
        media_type=f"image/{format}",
        headers={
            "Content-Disposition": f"attachment; filename=convertido.{format}"
        }
    )