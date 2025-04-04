from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer): # Creando un serializador para el modelo Usuario
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'telefono', 'first_name', 'last_name', 'password', 'rol', 'is_active', 'fecha_registro')
        extra_kwargs = {
            'password': {'write_only': True},  # Para que la contraseña no sea visible en la API
            'rol': {'read_only': True},  # No permitir que se establezca un rol directamente
            'is_active': {'read_only': True},  # No permitir que se establezca el estado directamente
            'fecha_registro': {'read_only': True},  # No permitir que se establezca la fecha de registro directamente
        }

    def create(self, validated_data):
        # Crear el usuario con contraseña encriptada
        user = Usuario.objects.create_user(**validated_data)
        return user

class UsuarioTokenSerializer(serializers.ModelSerializer): # Creando un serializador para los tokens del Usuario
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name']