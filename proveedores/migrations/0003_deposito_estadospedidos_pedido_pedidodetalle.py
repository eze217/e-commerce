# Generated by Django 3.2.8 on 2021-11-13 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_deposito', models.CharField(max_length=50, verbose_name='Nombre Deposito')),
            ],
        ),
        migrations.CreateModel(
            name='EstadosPedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(choices=[('pn', 'Pendiente'), ('TICKET_HISTORY', 'Ticket changed'), ('TICKET_RATE', 'Ticket rated'), ('PASSWORD_CHANGE', 'Password changed'), ('CONTENT', 'Added content')], max_length=20, verbose_name='Estado')),
                ('id_deposito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.deposito')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_total', models.FloatField(verbose_name='Monto (€)')),
                ('estado_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.estadospedidos')),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.producto')),
            ],
        ),
    ]
