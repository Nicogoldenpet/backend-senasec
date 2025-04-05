from django.db import models

# Modelo de fichas
class Ficha(models.Model):
    # Definición de los campos del modelo
    numero = models.CharField(max_length=8, unique=True, blank=False, null=False)  # Numero de la ficha

    def __str__(self):
        return self.numero # Devuelve el número de la ficha como representación del objeto
