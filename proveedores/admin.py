from django.contrib import admin
from .models import Proveedores,Producto
from .models import Deposito,Pedido,PedidoDetalle,EstadosPedidos

# Register your models here.


class ProveedoresAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')





admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Deposito)
admin.site.register(Pedido)
admin.site.register(PedidoDetalle)
admin.site.register(EstadosPedidos)



