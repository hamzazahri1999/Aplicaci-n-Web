from django.views.generic import ListView, DetailView
from .models import Servicio

class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicios/servicio_list.html'
    context_object_name = 'servicios'

class ServicioDetailView(DetailView):
    model = Servicio
    template_name = 'servicios/servicio_detail.html'
