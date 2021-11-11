from django.contrib import admin
from django.urls import path
from .views import proveedores, inactivo_proveedor, proveedoresPorEstado
from .views import ProveedorUpdateView, ProveedorFichaView,  ProductoListView, ProveedorCreateView, ProductoUpdateView, ProductoCreateView


urlpatterns = [
    
    path('', proveedores , name='proveedores'),
    path('<int:pk>/',ProveedorFichaView.as_view(), name='proveedor_ficha'),
    path('inactivo_proveedor/<int:id_proveedor>',inactivo_proveedor, name='inactivo_proveedor'),
    path('nuevo_proveedor/', ProveedorCreateView.as_view(), name='nuevo_proveedor'),
    path('<int:pk>/edito_proveedor/',ProveedorUpdateView.as_view(), name='edito_proveedor'),
    path('a/<int:estado>', proveedoresPorEstado, name='proveedoresPorEstado'),
    path('<int:pk>/productos/',ProductoListView.as_view(), name='productos_proveedor'),
    path('<int:pk>/edito_producto/',ProductoUpdateView.as_view(), name='edito_producto'),
    path('nuevo_producto/<int:pk>', ProductoCreateView.as_view(), name='nuevo_producto'),

]


