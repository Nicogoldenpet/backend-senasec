from rest_framework import viewsets
from .models import Ficha
from .serializers import FichaSerializer

# ViewSet para el modelo Ficha
class FichaViewSet(viewsets.ModelViewSet):
    queryset = Ficha.objects.all()  # Obtener todas las fichas
    serializer_class = FichaSerializer  # Usar el serializador FichaSerializer