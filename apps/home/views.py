from django.shortcuts import render
from gastos.models import Gastos
from ingresos.models import Ingresos
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Sum



# Create your views here.

def index(request):
    now=timezone.now()
     
    
    gastos_mensuales_total=Gastos.objects.filter(fecha_de_pago__month=now.month).aggregate(total=Sum('importe'))
    ingresos_mensuales_total=Ingresos.objects.filter(fecha_de_ingreso__month=now.month).aggregate(total=Sum('importe'))

    
    

    
        
        
    
    return render(request, 'home/index.html',{
        
        'gastos_mensuales':gastos_mensuales_total['total'], 
        'ingresos_mensuales': ingresos_mensuales_total['total']})

