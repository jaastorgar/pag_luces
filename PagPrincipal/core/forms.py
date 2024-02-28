from django import forms
from .models import Producto

class ProductoFilterForm(forms.Form):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), empty_label="Todos los productos", required=False)