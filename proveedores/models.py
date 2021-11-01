from django.db import models


class Proveedores (models.Model):
    nombre_proveedor = models.CharField(
        verbose_name='Nombre', max_length=50, blank=False)
    cif_proveedor = models.CharField(
        verbose_name='CIF', max_length=15, blank=False)
    domicilio_proveedor = models.CharField(
        verbose_name='Domicilio', max_length=50, blank=False)
    tel_proveedor = models.CharField(verbose_name='Telefono', max_length=10)
    mail_proveedor = models.EmailField(verbose_name='Email')
    estado_proveedor = models.BooleanField(verbose_name='activo', default=True)
    logo_proveedor = models.ImageField(
        verbose_name='Logo', blank=True, null=True, upload_to='proveedores_logos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre_proveedor