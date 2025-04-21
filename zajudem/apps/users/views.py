from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, permissions
from .models import Usuario
from .serializers import UsuarioSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from permissions.permissions import IsAdminUser

# Vista para Ver el Perfil del Usuario Autenticado
class ProfileView(APIView):  # Hereda de APIView para definir una vista más personalizada
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def get(self, request):  # Define el método GET para obtener los datos del usuario autenticado
        """
         ¿Qué hace este método?
        - Obtiene el usuario autenticado (`request.user`).
        - Devuelve los datos del usuario en formato JSON.
        - Agrega un mensaje de bienvenida personalizado.
        """
        user = request.user  # Obtiene el usuario que está haciendo la solicitud
        return Response({  # Retorna un JSON con los datos del usuario
            "message": f"¡Bienvenido, {user.username}!",  # Mensaje de bienvenida
            'username': user.username,
            'email': user.email,
            'telefono': user.telefono,
            'rol': user.rol
        })


class UsuarioCreateView(generics.CreateAPIView): # Vista para crear un usuario
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet): # Vista para ver todos los usuarios
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer