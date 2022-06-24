from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm


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


def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form': form})


def exito(request):
    return render(request, 'exito.html', {})
