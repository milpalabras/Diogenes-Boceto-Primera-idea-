from django.shortcuts import render

from .models import Ingresos, Cuenta
from .forms import Ingresosform, Cuentaform
from django.utils import timezone
from django.db.models import Sum
from django.http import HttpResponseRedirect

# Create your views here.

def InfoIngresos (request):
     now=timezone.now()
     
     ingresos_mensuales = Ingresos.objects.order_by('fecha_de_ingreso').filter(fecha_de_ingreso__month=now.month)
     ingresos_diarios = Ingresos.objects.order_by('fecha_de_ingreso').filter(fecha_de_ingreso__day=now.day)
     ingresos_mensuales_total=Ingresos.objects.filter(fecha_de_ingreso__month=now.month).aggregate(total=Sum('importe'))
     ingresos_anual_total=Ingresos.objects.filter(fecha_de_ingreso__year=now.year).aggregate(total=Sum('importe'))
     ingresos_diario_total=Ingresos.objects.filter(fecha_de_ingreso__day=now.day).aggregate(total=Sum('importe'))




     if request.method == 'POST':
          form = Ingresosform(request.POST)
          if form.is_valid(): 
               form.save(commit=False)
               importe = int(request.POST['importe'])
               cuenta_id = request.POST['cuenta']
               monto = Cuenta.objects.get(pk=cuenta_id)
               monto.monto += importe
               monto.save()               
               #monto_actual = Cuenta.objects.values_list('monto', flat=True).get(pk=cuenta_id)
               #cuenta_actualizado = Cuenta(pk=cuenta_id, monto=(monto_actual + importe) )
               #cuenta_actualizado.save()  
               form.save() 
               return HttpResponseRedirect('/')              
     else:
          form = Ingresosform()
    
     return render(request, 'ingresos/info_ingresos.html', {
          'form':form,
          'ingresos_mensuales': ingresos_mensuales,
          'ingresos_diarios': ingresos_diarios, 
          'ingresos_mensuales_total':ingresos_mensuales_total['total'],
          'ingresos_anual_total':ingresos_anual_total['total'],
          'ingresos_diarios_total':ingresos_diario_total['total'],
          
          
          
          } )


def infoCuentas (request):
     if request.method == 'POST':
          form = Cuentaform(request.POST)
          if form.is_valid():               
               form.save()
               return HttpResponseRedirect('/')
               
     else:
          
          form = Cuentaform()
          
          

     cuentas = Cuenta.objects.all()
    
     return render(request, 'ingresos/cuentas.html', {'form':form, 'cuentas':cuentas})