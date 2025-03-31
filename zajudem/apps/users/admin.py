from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    # Modelo asociado
    model = Usuario
    
    # Campos que se mostrarán en la lista de usuarios en el panel de administración
    list_display = ('username', 'email', 'celular', 'rol', 'is_active', 'is_staff')
    
    # Campos por los que se puede buscar en el panel de administración
    search_fields = ('email', 'celular')
    
    # Ordenar la lista de usuarios por el campo de correo electrónico
    ordering = ('email',)

# Registrar el modelo Usuario en el panel de administración
admin.site.register(Usuario, UsuarioAdmin)