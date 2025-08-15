from rest_framework import serializers
from .models import Ambiente

class AmbienteSerializer(serializers.ModelSerializer):  # Serializador para el modelo Ambiente
    class Meta:
        model = Ambiente
        fields = '__all__'  # Incluir todos los campos del modelo