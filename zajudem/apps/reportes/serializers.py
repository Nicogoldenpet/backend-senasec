from rest_framework import serializers
from .models import Reporte # Importando el modelo Reporte
from apps.programaciones.models import Programacion # Importando el modelo Programacion

class ReporteSerializer(serializers.ModelSerializer): # Serializador para el modelo Reporte
    programacion = serializers.PrimaryKeyRelatedField(queryset=Programacion.objects.none())

    class Meta:
        model = Reporte
        fields = '__all__'  # Incluir todos los campos del modelo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        if user.rol == 'admin':
            self.fields['programacion'].queryset = Programacion.objects.all()
        else:
            self.fields['programacion'].queryset = Programacion.objects.filter(usuario=user)