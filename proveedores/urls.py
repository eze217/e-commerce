from django.contrib import admin
from django.urls import path
from .views import proveedores, inactivo_proveedor, proveedoresPorEstado
from .views import ProveedorUpdateView, ProveedorFichaView,  ProductoListView, ProveedorCreateView, ProductoUpdateView, ProductoCreateView
from .views import PedidoCreateView, ConfirmoPedidoProveedor, PedidosView, DetallePedidoView, cambiaEstadoPedido

urlpatterns = [
    
    path('', proveedores , name='proveedores'),
    path('<int:pk>/',ProveedorFichaView.as_view(), name='proveedor_ficha'),
    path('inactivo_proveedor/<int:id_proveedor>',inactivo_proveedor, name='inactivo_proveedor'),
    path('nuevo_proveedor/', ProveedorCreateView.as_view(), name='nuevo_proveedor'),
    path('<int:pk>/edito_proveedor/',ProveedorUpdateView.as_view(), name='edito_proveedor'),
    path('a/<int:estado>', proveedoresPorEstado, name='proveedoresPorEstado'),

    path('productos/', ProductoListView.as_view(),name='productos'),
    path('<int:pk>/productos/',ProductoListView.as_view(), name='productos_proveedor'),
    path('<int:pk>/edito_producto/',ProductoUpdateView.as_view(), name='edito_producto'),
    path('nuevo_producto/<int:pk>', ProductoCreateView.as_view(), name='nuevo_producto_prov'),
    path('nuevo_producto/', ProductoCreateView.as_view(),name='nuevo_producto'),

    path('creo_orden/', PedidoCreateView.as_view(), name='creo_orden'),
    path('confirmo/',ConfirmoPedidoProveedor.as_view() , name='confirmo_compra'),

    path('pedidos/',PedidosView.as_view(),name='pedidos'),
    path('detalle_pedido/<int:pedido_id>',DetallePedidoView.as_view(), name='detalle_pedido'),
    
    path('cambiaEstadoPedido/<int:pedido_id>/<int:id_estado>',
         cambiaEstadoPedido, name='cambia_estado_pedido'),
    

]


