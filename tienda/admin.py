from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Marca
from .models import Producto
from .models import Compra

admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Compra)

