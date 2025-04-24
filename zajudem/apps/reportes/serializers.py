from rest_framework import serializers
from .models import Reporte # Importando el modelo Reporte
from apps.programacion.models import Programacion # Importando el modelo Programacion

class ProgramacionNestedSerializer(serializers.ModelSerializer):
    """Serializador anidado para desglosar los datos de Programacion."""
    usuario = serializers.StringRelatedField()  # Mostrar el nombre del usuario
    aula = serializers.StringRelatedField()  # Mostrar el aula
    ficha = serializers.StringRelatedField()  # Mostrar el número de la ficha

    class Meta:
        model = Programacion
        fields = ['usuario', 'aula', 'ficha']  # Campos que se desglosarán

class ReporteSerializer(serializers.ModelSerializer): # Serializador para el modelo Reporte
    programacion = ProgramacionNestedSerializer() # Usar el serializador anidado

    class Meta:
        model = Reporte
        fields = '__all__'  # Incluir todos los campos del modelo
        extra_kwargs = {
            'fecha_reporte': {'read_only': True},  # Para que la ultima actualizacion no sea visible en la API
        }