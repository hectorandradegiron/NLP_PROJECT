from django.contrib import admin
from django.urls import path

from . import views



app_name = "normas_app"

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('adjuntar/', views.CargarView.as_view(), name='adjuntar'),
    path('procesar/', views.ProcesarView.as_view(), name='procesar'),
    path('vertexto/<int:id>', views.TextoView.as_view(), name='vertexto'),
    


]