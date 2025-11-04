from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente

# Vista para listar todos los clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/lista_clientes.html'
    context_object_name = 'clientes'

# Vista para ver el detalle de un cliente
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/detalle_cliente.html'
    context_object_name = 'cliente'

# Vista para crear un nuevo cliente
class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'telefono', 'email']
    template_name = 'clientes/form_cliente.html'
    success_url = reverse_lazy('lista_clientes')

# Vista para actualizar un cliente existente
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'telefono', 'email']
    template_name = 'clientes/form_cliente.html'
    success_url = reverse_lazy('lista_clientes')

# Vista para borrar un cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/confirmar_borrado.html'
    success_url = reverse_lazy('lista_clientes')
