from django.shortcuts import render
from gastos.models import *
from .forms import Gastosform, Categoriaform
from ingresos.models import Cuenta
from django.utils import timezone
from django.db.models import Sum
from datetime import datetime
from django.http import HttpResponseRedirect


# Create your views here.



def infoGastos (request):
    
     now=timezone.now()
     
     gastos_mensuales = Gastos.objects.order_by('fecha_de_pago').filter(fecha_de_pago__month=now.month)
     gastos_diarios = Gastos.objects.order_by('fecha_de_pago').filter(fecha_de_pago__day=now.day)
     gastos_mensuales_total=Gastos.objects.filter(fecha_de_pago__month=now.month).aggregate(total=Sum('importe'))
     gastos_anual_total=Gastos.objects.filter(fecha_de_pago__year=now.year).aggregate(total=Sum('importe'))
     gastos_diario_total=Gastos.objects.filter(fecha_de_pago__day=now.day).aggregate(total=Sum('importe'))
       
     if request.method == 'POST':
          form = Gastosform(request.POST)
          if form.is_valid():
               form.save(commit=False)
               importe = int(request.POST['importe'])
               cuenta_id = request.POST['cuenta_a_debitar']
               monto = Cuenta.objects.get(pk=cuenta_id)
               monto.monto -= importe
               monto.save()
               form.save()
               return HttpResponseRedirect('/')
     else:
          form = Gastosform()
     return render (request, 'gastos/info_gastos.html',{
          'form':form, 
          'gastos_mensuales': gastos_mensuales,
          'gastos_diarios': gastos_diarios, 
          'gastos_mensuales_total':gastos_mensuales_total['total'],
          'gastos_anual_total':gastos_anual_total['total'],
          'gastos_diarios_total':gastos_diario_total['total']
     
     })


def infoCategorias (request):
     categorias = CategoriaGastos.objects.filter(parent__isnull=True)

     if request.method == 'POST':
          form = Categoriaform(request.POST)
          if form.is_valid():               
               form.save()
               return HttpResponseRedirect('/')
     else:
          form = Categoriaform()


     return render (request, 'gastos/categorias_gastos.html',{'form':form, 'categorias':categorias})


def Buscar (request):
    
     if request.GET.get('gasto'):
        busqueda = request.GET.get('gasto')
        gastos = Gastos.objects.filter(nota__icontains=busqueda)
        return render (request, 'gastos/resultados_busqueda.html', {'gastos':gastos, 'busqueda':busqueda})
    
     else:
        mensaje="No hay datos para buscar"
        
     return render (request, 'gastos/resultados_busqueda.html', {'mensaje': mensaje} )


