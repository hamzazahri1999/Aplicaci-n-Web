from django.urls import path
from .views import ServicioListView, ServicioDetailView

urlpatterns = [
    path('', ServicioListView.as_view(), name='servicio_list'),
    path('<int:pk>/', ServicioDetailView.as_view(), name='servicio_detail'),
]
