from rest_framework import viewsets, permissions
from .models import Product,Enterprise,User
from .serializers import ProductSerializer,EnterpriseSerializer,UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = Enterprise.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EnterpriseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer