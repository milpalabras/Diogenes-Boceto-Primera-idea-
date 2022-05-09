from django.contrib import admin
from .models import *
from mptt.admin import DraggableMPTTAdmin


# Register your models here.

#class CategoriaGastosAdmin (admin.ModelAdmin):
 #   list_display=('campomodelo', 'campomodelo', 'etc')
  #  search_fields=()

#class GastosAdmin(admin.ModelAdmin):
 #   list_filter =()
 #date_hierachy ="" breadcumb



admin.site.register(CategoriaGastos, DraggableMPTTAdmin)
admin.site.register(Gastos)
admin.site.register(Forma_de_pago)
admin.site.register(Etiqueta)