from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Definición de las opciones de rol
    ROL_CHOICES = [
        ('admin', 'Administrador'),
        ('instructor', 'Instructor'),
        ('seguridad', 'Guardia'),
        ('aseo', 'Limpieza'),
    ]
    
    # Campo para almacenar el rol del usuario
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='instructor') # user por default
    
    # Campo de correo electrónico único
    email = models.EmailField(unique=True)
    
    # Campo de número de celular único
    telefono = models.CharField(max_length=15, unique=True)

    # Campo de estado de usuario
    is_active = models.BooleanField(default=True) # Para activar/desactivar el usuario

    # Campo de fecha de registro
    fecha_registro = models.DateTimeField(auto_now=True) # Fecha de registro automática

    # Método save para establecer el rol predeterminado al crear un nuevo usuario
    def save(self, *args, **kwargs):
        if not self.pk:
            self.rol = 'instructor'
        super().save(*args, **kwargs)
