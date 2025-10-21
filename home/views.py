from django.shortcuts import render

# Create your views here.

from django.http import request
from tienda.models import Servicio

def home(request):
    # devolver todos los servicios disponibles
    servicios_disponible = Servicio.objects.all().filter(esta_disponible=True)#Obtener todos los servicios que están marcados como disponibles en la base de datos
    
    # Enviar la variable al template
    return render(request, "home/home.html",{ # render funcion con tres argumentos request, ruta template, diccionario(quí envías datos desde la vista hacia el template.) 
        'servicios_disponible': servicios_disponible # clave = variable html / valor= variable python
    }) 