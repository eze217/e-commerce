from django import forms
from django.db.models.base import Model
from .models import Proveedores


class ProveedorCreateForms(forms.ModelForm):
    class Meta:
        model=Proveedores
        fields = ('nombre_proveedor', 'cif_proveedor',
                  'domicilio_proveedor', 'tel_proveedor', 'mail_proveedor', 'estado_proveedor', 'logo_proveedor')
                  
