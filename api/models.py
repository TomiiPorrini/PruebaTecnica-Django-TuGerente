from django.db import models

# Create your models here.
class clientes(models.Model):
    nombre = models.CharField(null=False, max_length=200)
    apellido = models.CharField(null=False, max_length=200)
    dni = models.CharField(null=False, unique=True, max_length=20)
    telefono = models.CharField(null=False, max_length=20)

class habitacion(models.Model):
    numero = models.CharField(null=False, unique=True, max_length=5)
    descripcion = models.CharField(null=False, max_length=200)
    tarifa = models.FloatField(null=False)

class facturas(models.Model):
    Tipos_pagos = (('TC', 'Tarjeta de Crédito'),
    ('TD', 'Tarjeta de Débito'),
    ('EF', 'Efectivo'),
    ('TB', 'Transferencia Bancaria'),
    ('QR', 'Pago con QR'))

    id_habitacion = models.ForeignKey('habitacion', on_delete=models.CASCADE)
    id_cliente = models.ForeignKey('clientes', on_delete=models.CASCADE)
    dia_ingreso = models.DateTimeField(null=False)
    dia_egreso = models.DateTimeField(null=False)
    metodo_pago = models.CharField(null=False, max_length=2, choices=Tipos_pagos, default='TC')
    monto_total = models.FloatField(null=False, default=0)
 
class reserva(models.Model):
    estados = (('PEN', 'PENDIENTE'),
    ('PAG', 'PAGADO'),
    ('ELI', 'ELIMINADO'))

    estado = models.CharField(null=False, max_length=3, choices=estados, default='PEN') 
    id_factura = models.ForeignKey('facturas', on_delete=models.CASCADE)