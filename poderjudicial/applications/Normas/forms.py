
from django import forms
from .models import Expediente

class ExpedienteForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Expediente
        fields = ('expediente',)
       