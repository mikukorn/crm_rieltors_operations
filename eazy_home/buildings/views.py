from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [
    {'title': "Все дома", 'url_name': 'buildings'},
    {'title': "Добавить объект", 'url_name': 'add_building'}
]


def get_buildings(request):
    model = Building.objects.all()
    context = {
        'model': model,
        'menu': menu,
        'title': 'Все дома'
    }
    return render(request, 'buildings/index.html', context = context)


def add_building(request):
    if request.method == 'POST':
        form = AddBuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddBuildingForm()
    return render(request, 'buildings/add_building.html', {'form': form, 'menu': menu, 'title': 'Добавление объекта'})


# def add_flats(request):
#     if request.method == 'POST':
#         form = AddFlatsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddFlatsForm()
#     return render(request, 'buildings/add_flats.html', {'form': form, 'menu': menu, 'title': 'Добавление объекта'})


def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
