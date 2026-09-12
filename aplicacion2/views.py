from django.shortcuts import render
from django.http import HttpResponse

def vista_tres(request):
    return HttpResponse("<h1>Bienvenido a la Vista 3 de mi aplicación 2</h1>")

def vista_cuatro(request):
    return HttpResponse("<h1>Esta es la Vista 4 de mi aplicación 2</h1>")

# Create your views here.
