import os
from pathlib import Path
from PIL import Image

ruta = Path(__file__).resolve().parents[2] / "imagenes_prueba" / "prueba.png"

def convertirRGB(imagen):
    if imagen.mode == "RGBA":
        fondo = Image.new("RGB", imagen.size, (255, 255, 255))
        fondo.paste(imagen, mask=imagen.split()[3])  
        imagen = fondo  
    else:
        imagen = imagen.convert("RGB") 
    return imagen

def convertir_a_jpg(ruta_imagen, ruta_salida):
    im = Image.open(ruta_imagen)
    im = convertirRGB(im)
    ruta_salida = Path(ruta_salida)
    im.save(ruta_salida, "JPEG")
 
def convertir_a_png(ruta_imagen, ruta_salida):
    im = Image.open(ruta_imagen)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA")
    ruta_salida = Path(ruta_salida)
    im.save(ruta_salida, "PNG")

def convertir_a_webp(ruta_imagen, ruta_salida):
    im = Image.open(ruta_imagen)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA")
    ruta_salida = Path(ruta_salida)
    im.save(ruta_salida, "WEBP")
    
def convertir_a_tiff(ruta_imagen, ruta_salida):
    im = Image.open(ruta_imagen)
    im = convertirRGB(im)
    ruta_salida = Path(ruta_salida)
    im.save(ruta_salida, "TIFF") 

def convertir_a_gif(ruta_imagen, ruta_salida):
    im = Image.open(ruta_imagen)
    im.convert("P")
    ruta_salida = Path(ruta_salida)
    im.save(ruta_salida, "GIF") 

def convertir_a_bmp(ruta_imagen, ruta_salida):
    im = Image.open(ruta_imagen)
    im = convertirRGB(im)
    ruta_salida = Path(ruta_salida)
    im.save(ruta_salida, "BMP") 
    
def convertir_a_ico(ruta_imagen, ruta_salida):
    im = Image.open(ruta_imagen)
    ruta_salida = Path(ruta_salida)
    im.save(ruta_salida, "ICO") 
     
convertir_a_gif(ruta, "prueba_convertida.gif")


#Hacer validaciones a cada uno