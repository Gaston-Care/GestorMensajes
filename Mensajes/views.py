from django.http import HttpResponse
from django.shortcuts import render
from .models import Mensaje

# Create your views here.
def ver_mensajes_recibidos(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario='Gaston')
    return render(request, 'mensajes.html', {'mensajes': mensajes_recibidos})