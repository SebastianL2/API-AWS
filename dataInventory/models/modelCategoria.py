from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
