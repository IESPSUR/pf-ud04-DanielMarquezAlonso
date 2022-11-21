from django.conf import settings
from django.db import models
from django.utils import timezone


class Marca(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    unidades = models.PositiveIntegerField()
    modelo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=12,decimal_places=2)
    detalles = models.TextField(max_length=500,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre

class Compra(models.Model):
    producto = models.ForeignKey(Producto, models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    unidades = models.PositiveIntegerField()
    importe = models.IntegerField()

    def __str__(self):
        return str(self.fecha)



from django.db import models

# Create your models here.
