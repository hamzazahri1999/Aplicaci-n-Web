from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Servicio


# Listar servicios
class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicios/servicio_list.html'
    context_object_name = 'servicios'


# Detalle de un servicio
class ServicioDetailView(DetailView):
    model = Servicio
    template_name = 'servicios/servicio_detail.html'
    context_object_name = 'servicio'


# Crear servicio
class ServicioCreateView(CreateView):
    model = Servicio
    template_name = 'servicios/servicio_form.html'
    fields = ['nombre', 'precio']
    success_url = reverse_lazy('servicio_list')


# Editar servicio
class ServicioUpdateView(UpdateView):
    model = Servicio
    template_name = 'servicios/servicio_form.html'
    fields = ['nombre', 'precio']
    success_url = reverse_lazy('servicio_list')


# Eliminar servicio
class ServicioDeleteView(DeleteView):
    model = Servicio
    template_name = 'servicios/servicio_confirm_delete.html'
    success_url = reverse_lazy('servicio_list')
