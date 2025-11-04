from django.urls import path
from .views import (
    ClienteListView,
    ClienteDetailView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
)

urlpatterns = [
    path('', ClienteListView.as_view(), name='lista_clientes'),               # listar
    path('<int:pk>/', ClienteDetailView.as_view(), name='detalle_cliente'),   # detalle
    path('nuevo/', ClienteCreateView.as_view(), name='crear_cliente'),        # crear
    path('<int:pk>/editar/', ClienteUpdateView.as_view(), name='editar_cliente'),  # editar
    path('<int:pk>/borrar/', ClienteDeleteView.as_view(), name='borrar_cliente'),  # borrar
]
