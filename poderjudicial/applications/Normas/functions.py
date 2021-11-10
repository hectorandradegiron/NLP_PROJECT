import random
import string
import cv2
import pytesseract
from django.conf import settings
from os import remove
import os
import tempfile
from pdf2image import convert_from_path
from PIL import Image
from spacy.matcher import Matcher
from spacy.lang.es import Spanish
import spacy
import re 

def images_to_text(enlace):
 
    #codigo para windows, ubica donde esta tesseract
    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
      
    # cargar la imagen utilizando opencv
    image = cv2.imread(enlace)

    # extraer texto de la imagen en español
    text = pytesseract.image_to_string(image, lang ='spa')

    return text

def pdf_to_text(enlace):
    file_path = enlace
    output_path = settings.MEDIA_ROOT+ '/' + "rfldhrorjdjscmfjg.jpeg" 
        
    # save temp image files in temp dir, delete them after we are finished
    with tempfile.TemporaryDirectory() as temp_dir:
        # convert pdf to multiple image
        images = convert_from_path(file_path, output_folder=temp_dir)
        # save images to temporary directory
        temp_images = []
        for i in range(len(images)):
            image_path = f'{temp_dir}/{i}.jpg'
            images[i].save(image_path, 'JPEG')
            temp_images.append(image_path)
        # read images into pillow.Image
        imgs = list(map(Image.open, temp_images))
    # find minimum width of images
    min_img_width = min(i.width for i in imgs)
    # find total height of all images
    total_height = 0
    for i, img in enumerate(imgs):
        total_height += imgs[i].height
    # create new image object with width and total height
    merged_image = Image.new(imgs[0].mode, (min_img_width, total_height))
    # paste images together one by one
    y = 0
    for img in imgs:
        merged_image.paste(img, (0, y))
        y += img.height
    # save merged image
    merged_image.save(output_path)
    
    resultado = images_to_text(output_path)
    remove(output_path)

    return resultado


# segmenta el texto completo generado por el OCR
def segmenta_texto_completo(texto, cargo):
    nlp = Spanish()
    doc = nlp(texto)
    inicio = []
    fin = []
    texto = []
    for token in doc:
        if token.text =="SE":
            span_inicio = doc[token.i+1]
            
            if span_inicio.text == "RESUELVE":
                inicio.append(token.i)


    for token in doc:        
        if token.text =="Regístrese":
            span_fin = doc[token.i+1]

            if span_fin.text == ",":
                if token.i > inicio[0]:                 
                    fin.append(token.i)
  
    
    for  i in range(len(fin)):
        span = doc[inicio[i]:fin[i]]
        texto.append(span.text) 

    return discriminar_lista_texto(texto, cargo)




# extrae nombre de la persona del texto discriminado
def extrae_nombre_persona(texto):
    nlp = Spanish()
    doc = nlp(texto)
    inicio = 0
    fin = 0
    nombre = ""
    for token in doc:
        if token.text =="Designar":                   
            inicio =token.i


    for token in doc:        
        if token.text =="el":
            span_fin = doc[token.i+1]

            if span_fin.text == "puesto":                             
                fin = token.i
  
    
    
    span = doc[inicio:fin]
    nombre = span.text
    return nombre

    
    return 



# Función compara cada elemento de la lista con el cargo, para identificar el segmento de texto correcto
def discriminar_lista_texto(lista, textobuscar):
    nlp = spacy.load("es_core_news_md")
    doc1= nlp(textobuscar)    
    
    for  i in range(len(lista)):
        doc2= nlp(lista[i])   
        
        if doc1.similarity(doc2)>0.9:     
            texto = lista[i]

    return extrae_nombre_persona(texto)


# Función para reconcer género
def reconoce_genero(nombre):
    
    genero = "Indefinido"
    nlp = spacy.load("es_core_news_md")
    doc_femenino= nlp("a la señora") 
    doc_masculino= nlp("al señor") 
    doc_nombre = nlp(nombre)  
              
    if doc_femenino.similarity(doc_nombre)>0.6:     
        genero = "Femenino"
    if doc_masculino.similarity(doc_nombre)>0.5:     
        genero = "Masculino"

    return genero

def limpiar_nombre(texto):
    nlp = spacy.load("es_core_news_md")
    doc = nlp(texto)
    texto = ""
    for token in doc:
        if token.pos_ == "PROPN":
            texto = texto + token.text + " "
    
    return texto


        







