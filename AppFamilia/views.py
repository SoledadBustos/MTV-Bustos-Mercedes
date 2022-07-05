from django.http import HttpResponse
from django.shortcuts import render

from .models import Persona

# Create your views here.

def inicioApp(request):
    return render(request, 'AppFamilia/inicio.html')


def crearPersona(request):
    persona=Persona(nombre='Soledad', apellido='Bustos', edad=30)
    persona.save()
    texto= f"Se creo el familiar {persona.nombre} {persona.apellido} con edad {persona.edad}"
    return HttpResponse(texto)

def crearPersona_2(request):
    persona=Persona(nombre='Daniel', apellido='Perez', edad=25)
    persona.save()
    texto= f"Se creo el familiar 2 {persona.nombre} {persona.apellido} con edad {persona.edad}"
    return HttpResponse(texto)

def crearPersona_3(request):
    persona=Persona(nombre='Maria', apellido='Ortiz', edad=40)
    persona.save()
    texto= f"Se creo el familiar 3 {persona.nombre} {persona.apellido} con edad {persona.edad}"
    return HttpResponse(texto)  


