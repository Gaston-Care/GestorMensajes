from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def ver_mensajes_recibidos(request):
    return HttpResponse("hola")