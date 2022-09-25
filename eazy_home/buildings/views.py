from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

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
            #print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddBuildingForm()
    return render(request, 'buildings/add_building.html', {'form': form, 'menu': menu, 'title': 'Добавление объекта'})

def login(request):
    return HttpResponse("Авторизация")

# def get_building(request):
#     return HttpResponse('Страница дома')
#
# def get_flats(request):
#     return HttpResponse('Страница квартир')
#
# def get_flat(request):
#     return HttpResponse('Страница квартир')
#
# def pageNotFound(request, exceptions):
#     return HttpResponseNotFound('Страница не найдена')

