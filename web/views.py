from django.shortcuts import render
from .models import Flan


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    diccionario = {
        'flanes_publicos': flanes_publicos,
    }
    return render(request, 'index.html', diccionario)

def about(request):
    return render(request, 'about.html')

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    diccionario = {
        'flanes_privados': flanes_privados,
    }
    return render(request, 'welcome.html', diccionario)
