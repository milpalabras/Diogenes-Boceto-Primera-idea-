
from django import forms
from .models import Ingresos, Cuenta
import datetime

class Ingresosform(forms.ModelForm):
    

    class Meta:
        model = Ingresos
        fields = ('name', 'importe', 'cuenta', 'fecha_de_ingreso', 'nota' )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
            'cuenta': forms.Select(attrs={'class': 'form-control'}),
            'fecha_de_ingreso' : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'nota': forms.Textarea(attrs={'class': 'form-control'}),

        }
        

class Cuentaform (forms.ModelForm):

    class Meta:
        model = Cuenta
        fields = ('name', 'monto', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            


        }
        labels ={
            'name': "Nombre de la cuenta", 
            'monto': "Monto inicial de la cuenta"

        }


