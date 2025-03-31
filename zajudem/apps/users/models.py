from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Definición de las opciones de rol
    ROL_CHOICES = [
        ('admin', 'Administrador'),
        ('seguridad', 'Guardia'),
    ]
    
    # Campo para almacenar el rol del usuario
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='seguridad') # user por default
    
    # Campo de correo electrónico único
    email = models.EmailField(unique=True)
    
    # Campo de número de celular único
    celular = models.CharField(max_length=15, unique=True)

    # Método save para establecer el rol predeterminado al crear un nuevo usuario
    def save(self, *args, **kwargs):
        if not self.pk:
            self.rol = 'seguridad'
        super().save(*args, **kwargs)
