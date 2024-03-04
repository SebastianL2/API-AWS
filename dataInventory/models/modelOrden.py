from django.db import models
from .modelProduct import Product
class Orden(models.Model):
    nombre_pedido = models.CharField(max_length=200)
    fecha_pedido = models.DateField()
    ordenes=models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
