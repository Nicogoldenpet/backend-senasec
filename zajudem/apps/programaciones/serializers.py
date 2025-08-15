from rest_framework import serializers
from .models import Programacion

class ProgramacionSerializer(serializers.ModelSerializer): # Serializador para el modelo Programacion
    class Meta:
        model = Programacion
        fields = '__all__'  # Incluir todos los campos del modelo

    def validate(self, data):
        """
        Validar que no haya conflictos de programación en el mismo ambiente y hora.
        """

        ambiente = data['ambiente']
        dia = data['dia']
        hora_inicio = data['hora_inicio']
        hora_fin = data['hora_fin']

        # Obtener la instancia si estamos actualizando
        instance_id = self.instance.id if self.instance else None

        conflictos = Programacion.objects.filter(
            ambiente=ambiente,
            dia=dia,
            hora_inicio__lt=hora_fin,
            hora_fin__gt=hora_inicio
        ).exclude(id=instance_id)  # Excluirse a sí misma si está editando

        if conflictos.exists():
            raise serializers.ValidationError("Ya existe una programación en este ambiente que se cruza con este horario.")
        
        return data
    
    # def create(self, validated_data):
    #     """
    #     Crear una programación con la asignación correspondiente.
    #     """
    #     usuario = validated_data.pop('usuario')
    #     ficha = validated_data.pop('ficha')

    #     # Buscar o crear la asignación correspondiente
    #     try:
    #         print("Buscando asignación...")  # Depuración
    #         asignacion = Asignacion.objects.get(usuario=usuario, ficha=ficha)
    #     except Asignacion.DoesNotExist:
    #         print("Asignación no encontrada.")
    #         raise serializers.ValidationError("La ficha seleccionada no está asignada al usuario.")

    #     # Crear la programación con la asignación encontrada
    #     programacion = Programacion.objects.create(asignacion=asignacion, ficha=ficha, **validated_data)
    #     return programacion
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     request = self.context.get('request')  # Obtener la solicitud del contexto
    #     if request and request.data.get('usuario'):  # Verificar si se envió un usuario
    #         try:
    #             usuario_id = int(request.data.get('usuario'))
    #             queryset = Ficha.objects.filter(asignaciones__usuario_id=usuario_id)
    #             print(f"Fichas disponibles para el usuario {usuario_id}: {queryset}")  # Depuración
    #             self.fields['ficha'].queryset = queryset
    #         except ValueError:
    #             print("Usuario no válido")  # Depuración
    #             self.fields['ficha'].queryset = Ficha.objects.none()  # Si el usuario no es válido, no mostrar fichas