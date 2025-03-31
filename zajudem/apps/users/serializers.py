from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer): # Creando un serializador para el modelo Usuario
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'celular', 'first_name', 'last_name', 'password', 'rol']
        extra_kwargs = {
            'password': {'write_only': True},  # Para que la contraseña no sea visible en la API
            'rol': {'read_only': True},  # No permitir que se establezca un rol directamente
        }

    def create(self, validated_data):
        # Crear el usuario con contraseña encriptada
        user = Usuario.objects.create_user(**validated_data)
        return user

class UsuarioTokenSerializer(serializers.ModelSerializer): # Creando un serializador para los tokens del Usuario
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name']