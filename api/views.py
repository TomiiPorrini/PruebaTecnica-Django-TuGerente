from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import  Response


#import models
from .models import habitacion
from .models import clientes
from .models import facturas
from .models import reserva

#import serializers
from .serializers import habitacionSerializer
from .serializers import clientesSerializer
from .serializers import facturasSerializer
from .serializers import reservaSerializer


# Create your views here.
class Cliente(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        Clientes = clientes.objects.all()
        serializer = clientesSerializer(Clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = clientesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Cliente registrado", status=status.HTTP_201_CREATED) 
        return Response("Algun dato es inválido", status=status.HTTP_400_BAD_REQUEST)

class infoCliente(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, dni):
        cliente = clientes.objects.filter(dni = dni).first()
        if cliente:
            serializer = clientesSerializer(cliente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("no existe un cliente con ese DNI.", status=status.HTTP_404_NOT_FOUND)

class Habitaciones(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        Habitaciones = habitacion.objects.all()
        serializer = habitacionSerializer(Habitaciones, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        data = request.data
        serializer = habitacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Habitacion registrada", status=status.HTTP_201_CREATED) 
        return Response("Algun dato es inválido", status=status.HTTP_400_BAD_REQUEST)

class infoHabitacion(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, numero):
        Habitacion = habitacion.objects.filter(numero = numero).first()
        if Habitacion:
            serializer = habitacionSerializer(Habitacion)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No existe una habitacion con ese NUMERO.", status=status.HTTP_404_NOT_FOUND)

class Facturas(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        Facturas = facturas.objects.all()
        serializer = facturasSerializer(Facturas, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        data = request.data
        serializer = facturasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("factura registrada", status=status.HTTP_201_CREATED) 
        return Response("Algun dato es inválido", status=status.HTTP_400_BAD_REQUEST)

class infofacturas(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, dni):
        cliente_buscado = clientes.objects.filter(dni = dni).values().first()
        if cliente_buscado:
            id_cliente =  cliente_buscado['id']
            Facturas = facturas.objects.filter(id_cliente = id_cliente).first()
            if Facturas:
                serializer = facturasSerializer(Facturas)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("No existen facturas de ese cliente.", status=status.HTTP_404_NOT_FOUND)
        return Response("No existe un cliente con ese dni.", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, dni):
        cliente_buscado = clientes.objects.filter(dni = dni).values().first()
        if cliente_buscado:
            id_cliente =  cliente_buscado['id']
            Factura = facturas.objects.filter(id_cliente = id_cliente).first()
            if Factura:
                serializer = facturasSerializer(Factura)
                Factura.delete()
                return Response("Se ha eliminado la factura con éxito", status=status.HTTP_200_OK)
            else:
                return Response("No existen facturas de ese cliente.", status=status.HTTP_404_NOT_FOUND)
        return Response("No existe un cliente con ese dni.", status=status.HTTP_404_NOT_FOUND)

class Reserva(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        Reservas = reserva.objects.all()
        serializer = reservaSerializer(Reservas, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        data = request.data
        serializer = reservaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Reserva registrada", status=status.HTTP_201_CREATED) 
        return Response("Algun dato es inválido", status=status.HTTP_400_BAD_REQUEST)

class infoReserva(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, dni):
        cliente_buscado = clientes.objects.filter(dni = dni).values().first()
        if cliente_buscado:
            id_cliente =  cliente_buscado['id']
            Facturas = facturas.objects.filter(id_cliente = id_cliente).values().first()
            if Facturas:
                id_factura = Facturas['id']
                Reserva = reserva.objects.filter(id_factura = id_factura).first()
                if Reserva:
                    serializer = reservaSerializer(Reserva)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response("No existen reserva de ese cliente.", status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("No existen facturas de ese cliente, por lo tanto, tampoco reservas.", status=status.HTTP_404_NOT_FOUND)
            
        return Response("No existe un cliente con ese dni.", status=status.HTTP_404_NOT_FOUND)

class infoReservaEstado(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, estado):
        if estado in ['PEN', 'ELI', 'PAG']:
            Reservas = reserva.objects.filter(estado = estado).first()
            if Reservas:
                serializer = reservaSerializer(Reservas)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("No existen reservas con ese estado.", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("No existe ese estado, solo hay ELI, PEN, PAG.", status=status.HTTP_404_NOT_FOUND)
