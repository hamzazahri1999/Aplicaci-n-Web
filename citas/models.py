from django.db import models
from clientes.models import Cliente
from servicios.models import Servicio

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.cliente} - {self.servicio} ({self.fecha} {self.hora})"
