from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

User = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'telefono', 'rol', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            telefono=validated_data.get('telefono'),
            rol=validated_data.get('rol', 'instructor'),
            password=validated_data['password']
        )
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD  # <- Esto indica que usaremos el campo email

    def validate(self, attrs):
        # Sobrescribimos para usar 'email' y 'password'
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(request=self.context.get('request'), email=email, password=password)

        if not user:
            raise serializers.ValidationError("Credenciales inválidas, verifica tu correo y contraseña.")

        data = super().validate(attrs)
        data['user'] = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "rol": user.rol,
        }
        return data