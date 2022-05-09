from django import forms
from .models import CategoriaGastos, Gastos

class Gastosform(forms.ModelForm):

    class Meta:
        model = Gastos
        fields = ('importe', 'nota', 'fecha_de_pago', 'categoria','cuenta_a_debitar' )
        widgets = {
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
            'nota': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_de_pago' : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de pago', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'cuenta_a_debitar': forms.Select(attrs={'class': 'form-control'}),
            

        }

class Categoriaform (forms.ModelForm):

    class Meta:
        model = CategoriaGastos
        fields = ('name', 'parent', 'tipo_de_gasto')
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control', 'placeholder':'Categoria superior'}),
            'tipo_de_gasto': forms.Select(attrs={'class': 'form-control'}),


        }
        labels ={
            'name': "Nombre de la categoria", 
            'parent': "Categoria Padre"

        }
