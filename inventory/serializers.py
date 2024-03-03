from rest_framework import serializers
from .models import Product,Enterprise
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

class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['id','username','email','password', 'role']


