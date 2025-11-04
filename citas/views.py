from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cita

# Lista de citas
class CitaListView(ListView):
    model = Cita
    template_name = 'citas/cita_list.html'
    context_object_name = 'citas'

# Detalle de una cita
class CitaDetailView(DetailView):
    model = Cita
    template_name = 'citas/cita_detail.html'
    context_object_name = 'cita'

# Crear cita
class CitaCreateView(CreateView):
    model = Cita
    template_name = 'citas/cita_form.html'
    fields = ['cliente', 'servicio', 'fecha', 'hora']
    success_url = reverse_lazy('cita_list')

# Editar cita
class CitaUpdateView(UpdateView):
    model = Cita
    template_name = 'citas/cita_form.html'
    fields = ['cliente', 'servicio', 'fecha', 'hora']
    success_url = reverse_lazy('cita_list')

# Borrar cita
class CitaDeleteView(DeleteView):
    model = Cita
    template_name = 'citas/cita_confirm_delete.html'
    success_url = reverse_lazy('cita_list')
