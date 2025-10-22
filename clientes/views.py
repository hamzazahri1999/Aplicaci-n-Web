from django.shortcuts import render, redirect
from .forms import ClienteForm

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # guarda el cliente en la base de datos
            return redirect('clientes:registro_exitoso')
    else:
        form = ClienteForm()
    return render(request, 'clientes/registrar_cliente.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'clientes/registro_exitoso.html')
