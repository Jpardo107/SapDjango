from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenidos(request):
    numPersonas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenidos.html', {'numpersonas': numPersonas, 'personas':personas})
