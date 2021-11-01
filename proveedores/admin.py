from django.contrib import admin
from .models import Proveedores

# Register your models here.


class ProveedoresAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Proveedores, ProveedoresAdmin)
