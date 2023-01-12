from rest_framework import serializers
from .models import habitacion, clientes, facturas, reserva

class clientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientes
        fields = '__all__'

class facturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = facturas
        fields = '__all__'

class habitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = habitacion
        fields = '__all__'
        
class reservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = reserva
        fields = '__all__'