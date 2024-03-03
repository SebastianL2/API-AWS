from django.db import models
from .modelCategoria import Categoria

class Product(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=150)
    caracteristicas = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=3) 
    categorias=models.ManyToManyField(Categoria)
    created_at = models.DateTimeField(auto_now_add=True)
    