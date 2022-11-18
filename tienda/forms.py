from django import forms
from django.core.exceptions import ValidationError

from .models import Producto
from .models import Compra

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('unidades','importe',)

    def clean_minas(self):
        unidad = self.cleaned_data.get('unidades')
        if unidad is None:
            raise ValidationError("Has introducido más unidades del stock actual")
        return unidad

