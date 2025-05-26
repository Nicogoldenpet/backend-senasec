from rest_framework import viewsets
from .models import Asignacion  # Importando el modelo Asignacion
from .serializers import AsignacionSerializer  # Importando el serializador AsignacionSerializer
from rest_framework.permissions import IsAuthenticated  # Importando permisos de autenticación
from rest_framework.exceptions import PermissionDenied


# Vista para listar asignaciones con crud personalizado para administradores y usuarios
class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Verificar si el usuario está autenticado
        if self.request.user.is_authenticated:
            # Si el usuario es administrador, devolver todas las programaciones
            if self.request.user.rol == 'admin':  # Asegúrate de que el campo 'rol' exista en el modelo de usuario
                return Asignacion.objects.all()
            # Si no es administrador, devolver solo las programaciones del usuario logueado
            return Asignacion.objects.filter(usuario=self.request.user)
        # Si el usuario no está autenticado, devolver un queryset vacío
        raise PermissionDenied(detail="Debe iniciar sesión para acceder a esta área.")
    
    def create(self, request, *args, **kwargs):
        if request.user.rol != 'admin':
            raise PermissionDenied(detail="Solo los administradores pueden crear asignaciones.")
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        if request.user.rol != 'admin':
            raise PermissionDenied("Solo los administradores pueden modificar asignaciones.")
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        if request.user.rol != 'admin':
            raise PermissionDenied("Solo los administradores pueden eliminar asignaciones.")
        return super().destroy(request, *args, **kwargs)

