from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.fichas.models import Ficha # Importar el modelo Ficha

class Usuario(AbstractUser):
    # Definición de las opciones de rol
    ROL_CHOICES = [
        ('administrador', 'Administrador'),
        ('instructor', 'Instructor'),
        ('guardia', 'Guardia'),
        ('limpieza', 'Limpieza'),
    ]
    
    # Campo para almacenar el rol del usuario
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='instructor') # user por default

    # Campo de documento de identidad único
    #documento = models.CharField(max_length=20, unique=True) # Documento de identidad único
    
    # Campo de correo electrónico único
    email = models.EmailField(unique=True)
    
    # Campo de número de celular único
    telefono = models.CharField(max_length=15, unique=True)

    # Campo de estado de usuario
    is_active = models.BooleanField(default=True) # Para activar/desactivar el usuario

    # Campo de fecha de registro
    fecha_registro = models.DateTimeField(auto_now=True) # Fecha de registro automática

    USERNAME_FIELD = 'email'  # Define el campo que se usará para iniciar sesión
    REQUIRED_FIELDS = ['username']  # Campos requeridos al crear un usuario

    def __str__(self):
        return f"{self.username} - {self.documento}"
