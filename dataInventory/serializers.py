from rest_framework import serializers
from .models.modelCliente import Cliente
from .models.modelCategoria import Categoria
from .models.modelEmpresa import Enterprise
from .models.modelOrden import Orden
from .models.modelProduct import Product
from django.contrib.auth.models import User

class ProductSerializer ( serializers.ModelSerializer):
     class Meta:
          model= Product
          fields = ('__all__')
          read_only_field=('nit','created_at')

class EnterpriseSerializer ( serializers.ModelSerializer):
     class Meta:
          model= Enterprise
          fields = ('__all__')
          read_only_field=('nit','created_at')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['id','username','email','password']


