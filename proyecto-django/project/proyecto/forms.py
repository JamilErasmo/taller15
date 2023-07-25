from django import forms
from .models import Edificio, Propietario, Departamento

class EdificioForm(forms.ModelForm):
    class Meta:
        model = Edificio
        fields = '__all__'

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'
