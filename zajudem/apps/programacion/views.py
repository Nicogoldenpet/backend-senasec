from rest_framework import viewsets
from .models import Programacion  # Importando el modelo Programacion
from .serializers import ProgramacionSerializer  # Importando el serializador ProgramacionSerializer

# ViewSet para el modelo Programacion
class ProgramacionViewSet(viewsets.ModelViewSet):
    queryset = Programacion.objects.all()  # Obtener todas las Programacion
    serializer_class = ProgramacionSerializer  # Usar el serializador ProgramacionSerializer