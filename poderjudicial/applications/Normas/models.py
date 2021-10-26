from django.db import models

from django.db import models
from django.utils import timezone
from datetime import datetime
from datetime import date
from django.utils.timezone import localtime

from django.contrib.auth.models import User





# Create your models here.



class Expediente(models.Model):

    entidad=models.CharField(default= "Entidad", max_length=200, null=True, blank = True, verbose_name= "Entidad:")
    titulo=models.CharField(default= "Titulo", max_length=300, null=True, blank = True, verbose_name= "Titulo:")
    tipo_documento = models.CharField(default= "Tipo", max_length=50, null=True, blank = True, verbose_name= "Tipo Documento:")
    numero_documento = models.CharField(max_length=50, null=True, blank = True, verbose_name= "Número:")
    considerando = models.CharField(max_length=2000, null=True, blank = True, verbose_name= "Considerandos:")
    resuelve = models.CharField(max_length=2000, null=True, blank = True, verbose_name= "Se Resuelve:")
    fecha_documento = models.DateField( default= date.today,  verbose_name= "Fecha:")
    texto_completo = models.CharField(max_length=200, null=True, blank = True, verbose_name= "Texto Completo:")  
   
    expediente= models.FileField(upload_to='',  help_text="Adjuntar Archivo")
    estado=models.BooleanField(default=False)

    def __str__(self):
	    return self.titulo

    class Meta:
        verbose_name = "Expediente"
        ordering = ['-id']
