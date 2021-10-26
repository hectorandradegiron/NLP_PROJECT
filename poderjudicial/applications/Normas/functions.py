import random
import string
import cv2
import pytesseract
#from pdf2image import convert_from_path



def suma(size = 6, chars= string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars)  for _ in range(size))

def text(enlace):

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    #image = cv2.imread(r'C:\PODERJUDICIAL\NLP_PROJECT\poderjudicial\EXPEDIENTES\futuro.jpg')
    image = cv2.imread(enlace)
    
    text = pytesseract.image_to_string(image, lang ='spa')
    return text


"""  
def convertoimages(enlace):
    poppler_path = r'C:\Program Files\poppler-21.10.0\Library\bin'
    images = convert_from_path('example.pdf')
 
    for i in range(len(images)):
       
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')
    return images

"""






