from django.contrib import admin
from django.urls import path
from .views import proveedores, proveedor_ficha, inactivo_proveedor, ProveedorCreateView,EditProveedorView,proveedoresPorEstado



urlpatterns = [
    
    path('', proveedores , name='proveedores'),
    path('ficha_proveedor/<int:id_proveedor>', proveedor_ficha, name='proveedor_ficha'),
    path('inactivo_proveedor/<int:id_proveedor>',inactivo_proveedor, name='inactivo_proveedor'),
    path('nuevo_proveedor/', ProveedorCreateView.as_view(), name='nuevo_proveedor'),
    #path('edito_proveedor/', EditProveedorView.as_view(), name='edito_proveedor')
    path('a/<int:estado>', proveedoresPorEstado, name='proveedoresPorEstado'),

]


