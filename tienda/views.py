from django.shortcuts import render, get_object_or_404, redirect
# from django.views import generic

from tienda.forms import ProductoForm
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
            producto.save()
            return redirect('admin_listado', pk=producto)
    producto_form = ProductoForm(instance=producto)

    return render(request, 'tienda/admin/producto_detalle.html', {'producto_form': producto_form})


def admin_producto_nuevo(request):
    """


    form = ProductoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('admin_listado')

    return render(request, 'tienda/admin/producto_detalle.html', {'producto_form': form})
"""
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            productos = Producto.objects.filter().order_by('nombre')
            return render(request, 'tienda/admin/producto_detalle.html', {'productos': productos})
    else:
        form = ProductoForm()
    return render(request, 'tienda/admin/producto_detalle.html', {'producto_form': form})

def admin_producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('admin_listado')

