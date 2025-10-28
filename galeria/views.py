from django.views.generic import ListView, DetailView
from .models import Foto

class FotoListView(ListView):
    model = Foto
    template_name = 'galeria/foto_list.html'
    context_object_name = 'fotos'

class FotoDetailView(DetailView):
    model = Foto
    template_name = 'galeria/foto_detail.html'
