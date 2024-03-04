from django.db import models

class Orden(models.Model):
    nombre_pedido = models.CharField(max_length=200)
    fecha_pedido = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
