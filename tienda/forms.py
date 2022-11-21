
from django import forms
from django.core.exceptions import ValidationError

from .models import Producto
from .models import Compra

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"

"""
class CompraForm(forms.ModelForm):
    precio = forms.DecimalField()
    importe = forms.DecimalField()



    class Meta:
        model = Compra
        model = Producto
        fields = ('unidades','importe')
"""
class CompraForm(forms.Form):
    unidades = forms.FloatField(label='unidades')



