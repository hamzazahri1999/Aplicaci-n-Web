from django.urls import path
from .views import FotoListView, FotoDetailView

urlpatterns = [
    path('', FotoListView.as_view(), name='foto_list'),
    path('<int:pk>/', FotoDetailView.as_view(), name='foto_detail'),
]
