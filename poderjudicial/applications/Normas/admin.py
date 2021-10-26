from django.contrib import admin

# Register your models here.

from .models import Expediente


class ExpedienteAdmin (admin.ModelAdmin):
    list_display=("id", "entidad", "titulo", "tipo_documento", "numero_documento", "considerando", "resuelve", "resuelve", "fecha_documento", "texto_completo")
    #earch_fields=("nombre", "nombreabreviado" )

admin.site.register(Expediente, ExpedienteAdmin)