from django.shortcuts import render, get_object_or_404, redirect
# from django.views import generic

from tienda.forms import ProductoForm, CompraForm
from tienda.models import Producto


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html', {})


def admin_listado(request):
    producto = Producto.objects.all()
    return render(request, 'tienda/admin/listado.html', {'productos': producto})


def admin_producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            productos = Producto.objects.filter().order_by('nombre')
            return render(request, 'tienda/admin/listado.html', {'productos': productos})
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/admin/producto_detalle.html', {'form': form})



def admin_producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            productos = Producto.objects.filter().order_by('nombre')
            return render(request, 'tienda/admin/listado.html', {'productos': productos})
    else:
        form = ProductoForm()
    return render(request, 'tienda/admin/producto_detalle.html', {'form': form})


def admin_producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('admin_listado')



def compra_listado(request):
    producto = Producto.objects.all()
    return render(request, 'tienda/listado_compra.html', {'productos': producto})
def compra_producto(request, pk):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.save()
            productos = Producto.objects.filter().order_by('nombre')
            return render(request, 'tienda/compra_producto.html', {'productos': productos})
    else:
        form = CompraForm()
    return render(request, 'tienda/listado_compra.html', {'form': form})
