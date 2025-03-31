from datetime import datetime

from django.contrib.sessions.models import Session # Sesiones de usuario

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken # Importando la obtencion de tokens
from rest_framework.authtoken.models import Token

class Login(ObtainAuthToken): # Creando una vista para el inicio de sesión

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context={'request': request}) # Creando una instancia del serializador
        if login_serializer.is_valid(): # Si los datos del usuario son válidos
            user = login_serializer.validated_data['user']
            token,created = Token.objects.get_or_create(user = user) # Crea el token para el usuario si no existe
            user_serializer = UsuarioTokenSerializer(user)
            if created:
                return Response({
                    'token': token.key,
                    'user': user_serializer.data,
                    'message': 'Inicio de sesión exitoso' # Respuesta exitosa
                }, status = status.HTTP_201_CREATED)
            else:
                
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete() # Si el usuario ya tiene una sesión activa, se elimina la sesión anterior
                token.delete() # Si el token ya existe, se elimina y se crea uno nuevo
                token = Token.objects.create(user = user)
                return Response({
                    'token': token.key,
                    'user': user_serializer.data,
                    'message': 'Inicio de sesión exitoso'
                }, status = status.HTTP_201_CREATED)
                
                #return Response({'error': 'Ya ha iniciado sesión'}, status = status.HTTP_409_CONFLICT)
        else:
            return Response({'error': 'Credenciales inválidas'}, status = status.HTTP_400_BAD_REQUEST)
        
class Logout(APIView): # Vista para cerrar sesión

    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()

            if token: # Si el token existe
                user = token.user

                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete() # Si el usuario cierra sesión, se elimina el token

                token.delete() # Borra el token
                session_message = 'Sesiones de usuario eliminadas'
                token_message = 'Token eliminado'
                return Response({'token_message': token_message, 'session_message': session_message}, status = status.HTTP_200_OK) # Respuesta exitosa
            
            return Response({'error': 'No se ha encontrado un usuario con estas credenciales'}, 
                            status = status.HTTP_400_BAD_REQUEST) # Error si no encuentra el token
        except:
            return Response({'error': 'No se ha encontrado token en la petición'}, 
                            status = status.HTTP_409_CONFLICT) # Error si no encuentra el token en la petición

class UsuarioCreateView(generics.CreateAPIView): # Vista para crear un usuario
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet): # Vista para ver todos los usuarios
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer