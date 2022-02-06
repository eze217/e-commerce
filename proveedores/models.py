from django.db import models
from django.db.models import query_utils
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User




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
    usuario=models.ForeignKey(User,on_delete=CASCADE)

    class meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre_proveedor


class Producto (models.Model):
    id_proveedor=models.ForeignKey(Proveedores,on_delete=models.CASCADE)
    nombre_producto= models.CharField(verbose_name='Nombre',max_length=50,blank=False,null=False)
    imagen_producto = models.ImageField(
        verbose_name='Imagen', blank=True, null=True, upload_to='productos_imagenes')
    descripcion_producto = models.CharField(
        verbose_name='Descripcion', max_length=50, blank=False, null=False)
    precio_producto = models.FloatField(
        verbose_name='Precio', blank=False, null=False)
    disponible_producto=models.BooleanField(verbose_name='Disponible',default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre_producto





class Deposito(models.Model):
    nombre_deposito = models.CharField(verbose_name='Nombre Deposito',max_length=50)
    es_predefinido = models.BooleanField(default=False)
    domicilio_deposito=models.CharField(verbose_name='Domicilio',max_length=50)
    telefono_deposito=models.CharField(verbose_name='Telefono',max_length=12)
        
    def __str__(self):
        return self.nombre_deposito


class EstadosPedidos(models.Model):
   # opciones=[('Pendiente'),('Confirmado'),('Anulado'),('En Reparto'),('Entregado')]

    TYPE_CHOICES = (
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADO', 'Confirmado'),
        ('ANULADO', 'Anulado'),
        ('REPARTO', 'En Reparto'),
        ('ENTREGADO', 'Entregado')
    )

    nombre_estado = models.CharField(verbose_name='Estado', choices=TYPE_CHOICES, max_length=20)

    def __str__(self):
        return self.nombre_estado
   




class Pedido(models.Model):
   # numero_orden=models.IntegerField(verbose_name='Numero de orden') es el ID
   id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
   estado_pedido = models.ForeignKey( EstadosPedidos, on_delete=CASCADE)
   id_deposito = models.ForeignKey(Deposito, on_delete=CASCADE , blank=True, null=True)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)



class PedidoDetalle(models.Model):
    numeroPedido=models.ForeignKey(Pedido,on_delete=CASCADE,verbose_name='Número de Pedido')
    idproducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cant_pedida=models.IntegerField(verbose_name='Cantidad')

    def montoTotal(self):
        total = self.cant_pedida * self.idproducto.precio_producto
        return total
    

