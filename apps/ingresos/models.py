from django.db import models
from gastos.models import *

# Create your models here.

class Cuenta (models.Model):
    name = models.CharField(max_length=30)
    color = ColorField(default='#FF0000')
    #tipo_de_cuenta =
    monto= models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural="Cuentas"
    
    def __str__(self):
        return self.name

    


class Ingresos (models.Model):
    name = models.CharField(max_length=30)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    cuenta = models.ForeignKey('Cuenta', on_delete=models.CASCADE )
    #etiqueta = models.ForeignKey('gastos.Etiqueta',on_delete=models.CASCADE, null=True, blank=True )
    fecha_de_ingreso = models.DateField()
    nota = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="Ingresos"
    
    def __str__(self):
        return self.name