from django.urls import path
from .views import CitaListView, CitaDetailView

urlpatterns = [
    path('', CitaListView.as_view(), name='cita_list'),
    path('<int:pk>/', CitaDetailView.as_view(), name='cita_detail'),
]
