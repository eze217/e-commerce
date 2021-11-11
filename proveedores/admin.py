from django.contrib import admin
from .models import Proveedores,Producto

# Register your models here.


class ProveedoresAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')





admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Producto, ProductoAdmin)


