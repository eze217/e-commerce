# Generated by Django 3.2.8 on 2021-11-13 16:01

from django.db import migrations, models
import proveedores.models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0006_auto_20211113_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='id_producto',
            field=models.ForeignKey(on_delete=proveedores.models.Proveedores, to='proveedores.producto'),
        ),
    ]
