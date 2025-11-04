# galeria/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Foto

# Listar todas las fotos
class FotoListView(ListView):
    model = Foto
    template_name = 'galeria/foto_list.html'
    context_object_name = 'fotos'


# Ver detalle de una foto
class FotoDetailView(DetailView):
    model = Foto
    template_name = 'galeria/foto_detail.html'
    context_object_name = 'foto'


# Crear nueva foto
class FotoCreateView(CreateView):
    model = Foto
    template_name = 'galeria/foto_form.html'
    fields = ['titulo', 'imagen', 'descripcion']
    success_url = reverse_lazy('foto_list')


# Editar una foto
class FotoUpdateView(UpdateView):
    model = Foto
    template_name = 'galeria/foto_form.html'
    fields = ['titulo', 'imagen', 'descripcion']
    success_url = reverse_lazy('foto_list')


# Eliminar una foto
class FotoDeleteView(DeleteView):
    model = Foto
    template_name = 'galeria/foto_confirm_delete.html'
    success_url = reverse_lazy('foto_list')
