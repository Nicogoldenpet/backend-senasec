from rest_framework import viewsets
from .models import Reporte  # Importando el modelo Reporte
from .serializers import ReporteSerializer  # Importando el serializador ReporteSerializer
from permissions.permissions import IsOwner
from rest_framework.exceptions import PermissionDenied

# ViewSet para el modelo Reportes
class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()  # Obtener todos los Reportes
    serializer_class = ReporteSerializer  # Usar el serializador ReporteSerializer
    permission_classes = [IsOwner]  # Requiere autenticación y ser propietario

    def get_queryset(self):
        # Verificar si el usuario está autenticado
        if self.request.user.is_authenticated:
            # Si el usuario es administrador, devolver todas los reportes
            if self.request.user.rol == 'administrador':  # Asegúrate de que el campo 'rol' exista en el modelo de usuario
                return Reporte.objects.all()
            # Si no es administrador, devolver solo los reportes del usuario logueado
            return Reporte.objects.filter(programacion__usuario=self.request.user)
        # Si el usuario no está autenticado, devolver un queryset vacío
        raise PermissionDenied(detail="Debe iniciar sesión para ver sus reportes.")