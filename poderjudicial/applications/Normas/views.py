from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
import os
from django.conf import settings
from applications.Normas.models import Expediente
from .forms import ExpedienteForm
# importamos la función

from .functions import  images_to_text, pdf_to_text, segmenta_texto_completo, reconoce_genero, limpiar_nombre
 #Create your views here.

class CargarView(CreateView):
    template_name = 'cargarpdf.html'
    model = Expediente
    form_class = ExpedienteForm    
    success_url = reverse_lazy('normas_app:procesar')

    def get_context_data(self, **kwargs):
        context = super(CargarView, self).get_context_data(**kwargs)        
        context['form_class']= ExpedienteForm
        return context

class ProcesarView(ListView):
    template_name = 'procesar.html'
    model = Expediente
    #context_object_name = 'lista'
   
class TextoView(ListView):
    template_name = 'vertexto.html'
    model = Expediente
      
    def get_context_data(self, **kwargs):
        context = super(TextoView, self).get_context_data(**kwargs)
        id = self.kwargs.get('id',None)       
        
        lista= Expediente.objects.filter(id=id)
        context['lista'] = lista 
        for e in lista:
            enlace = settings.MEDIA_ROOT + '/' + str(e.expediente)
            fecha = str(e.fecha_documento)
        resultado = pdf_to_text(str(enlace))  
        cargo = "Jefa de Gabinete de Asesores de la Dirección Ejecutiva de la Autoridad para la Reconstrucción con Cambios"
        entidad ="PRESIDENCIA DEL CONSEJO DE MINSITROS"
        resultado = segmenta_texto_completo(resultado, cargo)
        context['fecha'] = fecha
        context['genero'] = reconoce_genero(resultado)  
        context['nombre'] = limpiar_nombre(resultado)
        context['cargo'] = cargo
        context['entidad'] = entidad


        return context


class HomeView(TemplateView):
    template_name = 'home.html'
   



