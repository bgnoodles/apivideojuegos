from django.db import models

# Create your models here.
class Videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    desarrollador = models.CharField(max_length=50)
    distribuidor = models.CharField(max_length=50)
    fecha = models.DateField()