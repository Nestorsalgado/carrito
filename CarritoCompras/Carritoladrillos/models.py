from django.db import models

# Create your models here.
class Propiedad(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    ladrillos = models.IntegerField()
    ladrillosEnventa = models.IntegerField()
    imagen= models.ImageField()

def __str__(self):
    return f'{self.nombre} -> {self.precio}'

