from django.shortcuts import render
from django.views import generic

from tienda.models import Producto


# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def admin_listado(request):
    producto = Producto.objects.all()
    return render(request,'tienda/admin/listado.html', { 'productos' : producto })

def admin_producto_detalle(request):
    return render(request,'tienda/admin/producto_detalle.html')

def admin_producto_nuevo(request):
    return render(request,'tienda/admin/producto_detalle.html')

def admin_producto_eliminar(request):
    return render(request,'tienda/admin/producto_detalle.html')










