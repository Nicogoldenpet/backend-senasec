from django.db import models
from apps.users.models import Usuario # Importando el modelo User
from apps.aulas.models import Aula # Importando el modelo Aula
from apps.fichas.models import Ficha # Importando el modelo Ficha

class Programacion(models.Model): # Creando el modelo Programacion
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='programacion') # Relacionando Usuario
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='programacion') # Relacionando Aula
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE, related_name='programacion') # Relacionando Ficha
    dia = models.DateField() # Campo para la fecha
    hora_inicio = models.TimeField() # Campo para la hora de inicio
    hora_fin = models.TimeField() # Campo para la hora de fin
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.usuario.first_name} - {self.aula.aula} - {self.ficha.numero}" # Retornando el nombre del usuario, el aula y la ficha