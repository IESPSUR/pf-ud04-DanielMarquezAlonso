from django.conf import settings
from django.db import models


class Marca(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    unidades = models.IntegerField()
    modelo = models.CharField(max_length=100)
    precio = models.IntegerField()
    detalles = models.TextField(blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE())


    def __str__(self):
        return self.nombre

class Compra(models.Model):
    fecha = models.DateField()
    unidades = models.ForeignKey(Producto, on_delete=models.CASCADE())
    importe = models.IntegerField()

    def __str__(self):
        return self.fecha



from django.db import models

# Create your models here.
