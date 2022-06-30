from django.shortcuts import render
from .models import Flan, ContactForm, Local
from .forms import ContactFormModelForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    diccionario = {
        'flanes_publicos': flanes_publicos,
    }
    return render(request, 'index.html', diccionario)


def about(request):
    return render(request, 'about.html')


@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    diccionario = {
        'flanes_privados': flanes_privados,
    }
    return render(request, 'welcome.html', diccionario)


def contact(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactFormModelForm()
    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'success.html', {})


def location(request):
    locales = Local.objects.all()
    diccionario = {
        'locales': locales,
    }
    return render(request, 'location.html', diccionario)
