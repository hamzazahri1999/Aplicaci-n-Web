# galeria/urls.py
from django.urls import path
from .views import (
    FotoListView, FotoDetailView,
    FotoCreateView, FotoUpdateView, FotoDeleteView
)

urlpatterns = [
    path('', FotoListView.as_view(), name='foto_list'),
    path('<int:pk>/', FotoDetailView.as_view(), name='foto_detail'),
    path('crear/', FotoCreateView.as_view(), name='foto_create'),
    path('<int:pk>/editar/', FotoUpdateView.as_view(), name='foto_update'),
    path('<int:pk>/borrar/', FotoDeleteView.as_view(), name='foto_delete'),
]
