import os
from pathlib import Path
from PIL import Image

ruta = Path(__file__).resolve().parents[2] / "imagenes_prueba" / "prueba.png"

formatos = ["jpg", "jpeg", "png", "webp", "tiff", "tif", "gif", "bmp", "ico"]

def convertirImagen(imagen,formato): 
    if formato not in formatos:
        raise ValueError(f"Formato no soportado: {formato}")
    
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
    im = Image.open(ruta_imagen)
    im = convertirImagen(im, formato.lower())
    ruta_salida = Path(ruta_salida)
    im.save(ruta_salida, formato.upper())
    
convertir_a_formato(ruta, "prueba_convertida.gif", "ico")