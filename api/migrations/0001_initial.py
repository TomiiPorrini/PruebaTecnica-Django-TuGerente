# Generated by Django 4.1 on 2023-01-12 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='facturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_ingreso', models.DateTimeField()),
                ('dia_egreso', models.DateTimeField()),
                ('metodo_pago', models.CharField(choices=[('TC', 'Tarjeta de Crédito'), ('TD', 'Tarjeta de Débito'), ('EF', 'Efectivo'), ('TB', 'Transferencia Bancaria'), ('QR', 'Pago con QR')], default='TC', max_length=2)),
                ('monto_total', models.FloatField(default=0)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=5, unique=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('tarifa', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('PEN', 'PENDIENTE'), ('PAG', 'PAGADO'), ('ELI', 'ELIMINADO')], default='PEN', max_length=3)),
                ('id_factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.facturas')),
            ],
        ),
        migrations.AddField(
            model_name='facturas',
            name='id_habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.habitacion'),
        ),
    ]
