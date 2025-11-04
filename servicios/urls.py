from django.urls import path
from .views import (
    ServicioListView,
    ServicioDetailView,
    ServicioCreateView,
    ServicioUpdateView,
    ServicioDeleteView
)

urlpatterns = [
    path('', ServicioListView.as_view(), name='servicio_list'),
    path('<int:pk>/', ServicioDetailView.as_view(), name='servicio_detail'),
    path('crear/', ServicioCreateView.as_view(), name='servicio_create'),
    path('<int:pk>/editar/', ServicioUpdateView.as_view(), name='servicio_update'),
    path('<int:pk>/eliminar/', ServicioDeleteView.as_view(), name='servicio_delete'),
]
