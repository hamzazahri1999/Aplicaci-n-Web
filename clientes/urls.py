from django.urls import path
from .views import ClienteListView, ClienteDetailView

urlpatterns = [
    path('', ClienteListView.as_view(), name='lista_clientes'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='detalle_cliente'),
]
