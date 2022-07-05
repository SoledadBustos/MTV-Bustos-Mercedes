from django.contrib import admin
from django.urls import path, include

from .views import crearPersona, crearPersona_2, crearPersona_3, inicioApp


urlpatterns = [
    
    path('',inicioApp),
    path('crearPersona/', crearPersona),
    path('crearPersona_2/', crearPersona_2),
    path('crearPersona_3/', crearPersona_3),

]