from rest_framework import serializers
from .models import Programacion

class ProgramacionSerializer(serializers.ModelSerializer): # Serializador para el modelo Programacion
    usuario = serializers.StringRelatedField()  # Mostrar el nombre del usuario en lugar del ID
    aula = serializers.StringRelatedField() # Mostrar el aula
    ficha = serializers.StringRelatedField() # Mostrar el numero de la ficha
    
    class Meta:
        model = Programacion
        fields = '__all__'  # Incluir todos los campos del modelo
        extra_kwargs = {
            'ultima_actualizacion': {'read_only': True},  # Para que la ultima actualizacion no sea visible en la API
        }

    def validate(self, data):
        """
        Validar que no haya conflictos de programación en la misma aula y hora.
        """
        if Programacion.objects.filter(
            aula=data['aula'],
            dia=data['dia'],
            hora_inicio__lt=data['hora_fin'],
            hora_fin__gt=data['hora_inicio']
        ).exists():
            raise serializers.ValidationError("Ya existe una programación en este aula y horario.")
        return data