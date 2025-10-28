from django.views.generic import ListView, DetailView
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
