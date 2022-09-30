from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import *
from .models import *

menu = [
    {'title': "Все дома", 'url_name': 'buildings'},
    {'title': "Добавить объект", 'url_name': 'add_estate'}
]

def add_estate(request):
    if request.method == 'POST':
        form = AddEstateForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Объект успешно добавлен!')
            return HttpResponseRedirect(reverse_lazy('add_estate'))
    else:
        form = AddEstateForm()
    return render(request, 'buildings/add_building.html', {'form': form, 'menu': menu, 'title': 'Добавление объекта'})

def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Клиент успешно добавлен!')
            return HttpResponseRedirect(reverse_lazy('add_estate'))
    else:
        form = AddEstateForm()
    return render(request, 'buildings/add_building.html', {'form': form, 'menu': menu, 'title': 'Добавление объекта'})

def get_buildings(request):
    model = Estate.objects.all()
    context = {
        'model': model,
        'menu': menu,
        'title': 'Все дома'
    }
    return render(request, 'buildings/estate.html', context = context)



def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
