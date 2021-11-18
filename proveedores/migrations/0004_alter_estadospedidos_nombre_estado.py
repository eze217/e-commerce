# Generated by Django 3.2.8 on 2021-11-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0003_deposito_estadospedidos_pedido_pedidodetalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadospedidos',
            name='nombre_estado',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('CONFIRMADO', 'Confirmado'), ('ANULADO', 'Anulado'), ('REPARTO', 'En Reparto'), ('ENTREGADO', 'Entregado')], max_length=20, verbose_name='Estado'),
        ),
    ]
