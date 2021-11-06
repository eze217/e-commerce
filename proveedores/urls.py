from django.contrib import admin
from django.urls import path
from .views import proveedores, inactivo_proveedor, ProveedorCreateView, ProveedorUpdateView, ProveedorFichaView, proveedoresPorEstado



urlpatterns = [
    
    path('', proveedores , name='proveedores'),
    path('<int:pk>/',ProveedorFichaView.as_view(), name='proveedor_ficha'),
    path('inactivo_proveedor/<int:id_proveedor>',inactivo_proveedor, name='inactivo_proveedor'),
    path('nuevo_proveedor/', ProveedorCreateView.as_view(), name='nuevo_proveedor'),
    path('<int:pk>/edito_proveedor/',ProveedorUpdateView.as_view(), name='edito_proveedor'),
    path('a/<int:estado>', proveedoresPorEstado, name='proveedoresPorEstado'),

]


