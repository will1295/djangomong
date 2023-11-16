from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    carnet = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
