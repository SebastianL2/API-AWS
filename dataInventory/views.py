from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

from django.contrib.auth.models import User
from .models.modelProduct import Product

from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

@api_view(['POST'])
def login(request):

    user=get_object_or_404(User,email=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({"error":"contraseña incorrecta"},status=status.HTTP_400_BAD_REQUEST)
    token,created= Token.objects.get_or_create(user=user)
    serializer=UserSerializer(instance=user)
    data = serializer.data
    data['token'] = token.key
    return Response({"Token": token.key ,"user":data,"mensaje":"Sesión iniciada correctamente"},
                    status=status.HTTP_200_OK)

@api_view(['POST'])
def login2(request):

    user=get_object_or_404(User,email=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({"error":"contraseña incorrecta"},status=status.HTTP_400_BAD_REQUEST)
    token,created= Token.objects.get_or_create(user=user)
    serializer=UserSerializer(instance=user)
    data = serializer.data
    data['token'] = "no permitido"
    return Response({"Token": token.key ,"user":data,"mensaje":"Sesión iniciada correctamente"},
                    status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    email = request.data.get('email', '')  # Obtener el correo electrónico del cuerpo de la solicitud
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Este correo electrónico ya está en uso'}, status=status.HTTP_400_BAD_REQUEST)
  
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        # Obtener el usuario recién creado
        user = User.objects.get(username=serializer.data['username'])

        # Establecer y guardar la contraseña del usuario
        user.set_password(serializer.data['password'])
        user.save()

        # Crear un token para el usuario
        token = Token.objects.create(user=user)

        # Devolver la respuesta con el usuario y el token
        return Response({
            'mensaje': 'Usuario creado correctamente',
            'user': serializer.data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)
        
    return Response({'error': 'Este nombre electrónico ya está en uso'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):

    return Response("Estas Logeado con {}".format(request.user.username),status=status.HTTP_200_OK)


