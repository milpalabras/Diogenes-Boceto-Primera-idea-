from django.urls import path
from ingresos import views

urlpatterns = [  
        
    path('cuentas', views.infoCuentas, name="cuentas"),
    path('info_ingresos', views.InfoIngresos, name="info_ingresos"),  
    
]