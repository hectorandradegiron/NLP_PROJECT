from django.shortcuts import render
from django.views.generic import TemplateView

 #Create your views here.

class CargarView(TemplateView):
    template_name = 'cargarpdf.html'


