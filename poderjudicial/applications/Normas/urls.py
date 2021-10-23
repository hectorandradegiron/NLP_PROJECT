from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('cargar/', views.CargarView.as_view()),
]