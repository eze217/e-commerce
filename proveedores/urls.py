from django.contrib import admin
from django.urls import path
from .views import proveedores,proveedor_ficha,inactivo_proveedor



urlpatterns = [
    
    path('', proveedores , name='proveedores'),
    path('ficha_proveedor/<int:id_proveedor>', proveedor_ficha, name='proveedor_ficha'),
    path('inactivo_proveedor/<int:id_proveedor>',inactivo_proveedor, name='inactivo_proveedor')

]


