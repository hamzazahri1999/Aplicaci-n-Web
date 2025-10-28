from django.views.generic import ListView, DetailView
from .models import Cita

class CitaListView(ListView):
    model = Cita
    template_name = 'citas/cita_list.html'
    context_object_name = 'citas'

class CitaDetailView(DetailView):
    model = Cita
    template_name = 'citas/cita_detail.html'
