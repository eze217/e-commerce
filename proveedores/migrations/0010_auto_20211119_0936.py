# Generated by Django 3.2.8 on 2021-11-19 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0009_proveedores_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='id_proveedor',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='monto_total',
        ),
        migrations.RemoveField(
            model_name='pedidodetalle',
            name='valor_producto',
        ),
        migrations.RemoveField(
            model_name='pedidodetalle',
            name='valor_producto_total',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado_pedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.estadospedidos'),
        ),
    ]
