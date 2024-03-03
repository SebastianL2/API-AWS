from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
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
def register(request):
    serializer= UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'mensaje': 'Usuario Creado correctamente','user': serializer.data,'token':token.key},status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def profile(request):
    return Response({})