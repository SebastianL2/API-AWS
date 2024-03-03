from django.db import models

class Enterprise(models.Model):
    nit = models.CharField(max_length=150, primary_key=True) 
    name = models.TextField(null=True, blank=True)
    direccion = models.TextField(default=False)
    telefono = models.TextField(max_length=15,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
