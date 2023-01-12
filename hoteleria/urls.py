"""hoteleria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views as api_views

urlpatterns = [
    path("admin", admin.site.urls),
    path("api/cliente/", api_views.Cliente.as_view(), name='cliente'),
    path("api/cliente/<int:dni>", api_views.infoCliente.as_view(), name='info_cliente'),
    path("api/habitacion/", api_views.Habitaciones.as_view(), name='habitacion'),
    path("api/habitacion/<int:numero>", api_views.infoHabitacion.as_view(), name='info_habitacion'),
    path("api/facturas/", api_views.Facturas.as_view(), name='facturas'),
    path("api/facturas/cliente/<int:dni>", api_views.infofacturas.as_view(), name='facturas_cliente'),
    path("api/reserva/", api_views.Reserva.as_view(), name='reserva'),
    path("api/reserva/cliente/<int:dni>", api_views.infoReserva.as_view(), name='reserva_cliente'),
    path("api/reserva/estado/<str:estado>", api_views.infoReservaEstado.as_view(), name='reserva_estado'),
]
