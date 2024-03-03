from django.db import models
from .modelOrden import Orden
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    ordenes=models.ManyToManyField(Orden)
    created_at = models.DateTimeField(auto_now_add=True)
