# PruebaTecnica-Django-TuGerente
Prueba técnica desarrollado en Django(Python) para TuGerente

## Problematica: 
Utilizando Django Rest Framework, desarrollá los endpoints para el sistema de reservas de habitación de un hotel
* CONDICIONES:

- Las reservas pueden tener 3 estados: Pendiente, Pagado y Eliminado.
- Los datos a almacenar para la reserva son: los detalles del cuarto reservado, los días de estadía, los datos de facturación e identificación del cliente, el monto pagado y el método de pago.
- Proponé los endpoints a crearse para tratar de cubrir el flujo normal de operación de reserva y explicar por qué. 
- El proyecto debe correrse en un contenedor de docker, se puede usar cualquier gestor de base de datos relacionales
- Adjuntar también un archivo con ejemplos de consumo de la API para Postman

## Cuenta de admin:
* usuario: user
* contraseña: user
## ENDPOINTS PROPUESTOS:
> Cada endpoint tiene su link para realizar su consumo en postman. Por defecto, los va a llevar al login de admin.
1. LISTAR CLIENTES (GET): http://127.0.0.1:8000/api/cliente/
2. OBTENER INFO DE UN CLIENTE (GET): http://127.0.0.1:8000/api/cliente/11223344
3. CREAR CLIENTE (POST): http://127.0.0.1:8000/api/cliente/, INGRESANDO ESTE JSON:
```{
    "nombre": "COMPLETAR",
    "apellido": "COMPLETAR",
    "dni": "COMPLETAR",
    "telefono": "COMPLETAR"
}
```
4. OBTENER LISTA DE HABITACIONES (GET): http://127.0.0.1:8000/api/habitacion/
5. OBTERNER INFO DE UNA HABITACION (GET): http://127.0.0.1:8000/api/habitacion/NumHabitacion (2 or 3)
6. CREAR HABITACION (POST): http://127.0.0.1:8000/api/habitacion/, INGRESANDO ESTE JSON:
```{
    "numero": "COMPLETAR",
    "descripcion": "COMPLETAR",
    "tarifa": "COMPLETAR",
}
```
7. OBTENER FACTURA DE UN CLIENTE (GET): http://127.0.0.1:8000/api/facturas/cliente/DNI (123123123 or 11223344)
8. OBTENER LISTA DE FACTURAS (GET): http://127.0.0.1:8000/api/facturas
9. CREAR FACTURA (POST): http://127.0.0.1:8000/api/facturas, INGRESANDO ESTE JSON:
```
{
    "id_habitacion": "COMPLETAR",
    "id_cliente": "COMPLETAR",
    "dia_ingreso":"2023-01-18 10:53:00", (Dejo esta fecha para que sea una guia del formato.)
    "dia_egreso":"COMPLETAR",
    "metodo_pago":"COMPLETAR",
    "monto_total": "COMPLETAR"
}
```
10. ELIMINAR UNA FACTURA DE UN CLIENTE (DELETE): http://127.0.0.1:8000/api/facturas/cliente/DNI (123123123 or 11223344)
> aclaración: Borra la primer factura encontrada, es decir, la que tenga el menor id.
11. OBTENER TODAS LAS RESERVAS (GET): http://127.0.0.1:8000/api/reserva/
12. CREAR UNA RESERVA (POST): http://127.0.0.1:8000/api/reserva/, INGRESANDO ESTE JSON:
```
{
    "estado": "COMPLETAR CON 3 LETRAS.",(PEN -> PENDIENTE, PAG -> PAGADO, ELI -> ELIMINADO)
    "id_factura":"COMPLETAR"
}
```
13. OBTENER TODAS LAS RESERVAS CON UN ESTADO (GET): http://127.0.0.1:8000/api/reserva/estado/estado (ELI or PAG or PEN)
14. OBTENER UNA RESERVA DE UN CLIENTE (GET): http://127.0.0.1:8000/api/reserva/cliente/DNI (123123123 or 11223344)
> No hace falta, eliminar una reserva, ya que esté utilizado con el parametro on_delete:CASCADE, por lo que si se borra una factura que hace referencia a alguna reserva, esta se borraria automaticamente.



## Diagrama de entidad-relacion (DER), creado de guía:
![DER](https://user-images.githubusercontent.com/105433665/212089815-77c34518-26c0-4ce4-bddf-0603ebc729b8.png)
