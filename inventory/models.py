from django.db import models

# Create your models here.
from django.db import models
from rest_framework.decorators import action
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150) 
    description =models.TextField(null=True,blank=True)
    done=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Enterprise(models.Model):
    nit = models.CharField(max_length=150, primary_key=True) 
    name = models.TextField(null=True, blank=True)
    direccion = models.TextField(default=False)
    telefono = models.TextField(max_length=15,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class User(AbstractUser):
    ADMINISTRADOR = 'administrador'
    EXTERNO = 'externo'

    ROLE_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (EXTERNO, 'Externo'),
    ]

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default=EXTERNO)