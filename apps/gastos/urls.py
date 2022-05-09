from django.urls import path
from gastos import views

urlpatterns = [
    
    
    path('info_gastos', views.infoGastos, name="info_gastos"),
    path('categorias', views.infoCategorias, name = "categoria_gastos"),
    path('buscar/', views.Buscar),
        
    
     
    
]