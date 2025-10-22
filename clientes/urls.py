from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('exitoso/', views.registro_exitoso, name='registro_exitoso'),
]
