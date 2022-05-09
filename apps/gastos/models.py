from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CategoriaGastos(MPTTModel):
    name = models.CharField(max_length=30)
    parent = TreeForeignKey ('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    #tipo = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='icon_categoriagastos', null=True, blank=True)
    color = ColorField(default='#FF0000')
    
    class Tipodegasto (models.TextChoices):
        FIJO ='F', _('Fijo-Obligatorio')
        NECESIDAD = 'N', _('Necesario-Sobrevivencia')
        PRESCINDIBLE = 'P',_('Prescindible-Lujo')
        PADRE = 'A',_('Categoria Padre')
    
    tipo_de_gasto = models.CharField(max_length=1, choices=Tipodegasto.choices, default=Tipodegasto.FIJO)

    class MPTTMeta:
        order_insertion_by=['name']

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

    

class Etiqueta(models.Model):
    name = models.CharField(max_length=50)
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name_plural="Etiquetas"

    def __str__(self):
        return self.name


class Forma_de_pago(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural="Forma de pagos"
    
    def __str__(self):
        return self.name


class Gastos (models.Model):
    importe = models.DecimalField(max_digits=10,  decimal_places=2)
    nota = models.CharField(max_length=30, blank=True, null=True)
    fecha_de_pago = models.DateField()
    categoria = models.ForeignKey("CategoriaGastos", on_delete=models.CASCADE, null=True)
    cuenta_a_debitar = models.ForeignKey('ingresos.Cuenta', on_delete=models.CASCADE, null=True)
    #etiqueta = models.ForeignKey('Etiqueta',on_delete=models.CASCADE, null=True, blank=True )
    #forma_de_pago = models.ForeignKey('Forma_de_pago', on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        verbose_name_plural = "Gastos"

    def __str__(self):
        return self.categoria.name