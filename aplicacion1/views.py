from django.shortcuts import render
from django.http import HttpResponse

def vista_uno(request):
    return HttpResponse("<h1>Hola, esta es la Vista 1 de mi primera aplicación</h1>")

def vista_dos(request):
    return HttpResponse("<h1>Esta es la Vista 2 de mi primera aplicación</h1>")

# Create your views here.
