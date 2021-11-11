from django import forms
from django.db.models.base import Model
from django.db.models.query import QuerySet
from .models import Producto, Proveedores


class ProveedorCreateForms(forms.ModelForm):
    class Meta:
        model=Proveedores
        fields = ('nombre_proveedor', 'cif_proveedor',
                  'domicilio_proveedor', 'tel_proveedor', 'mail_proveedor', 'estado_proveedor', 'logo_proveedor')
                  


class ProductoCreateForms(forms.ModelForm):
    class Meta:
        model= Producto
        fields = ('id_proveedor', 'nombre_producto', 'descripcion_producto',
                  'precio_producto', 'disponible_producto', 'imagen_producto')


class ProductoProveedorCreateForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre_producto', 'descripcion_producto',
                  'precio_producto', 'disponible_producto', 'imagen_producto')



