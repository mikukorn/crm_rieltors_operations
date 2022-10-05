from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import *
from .models import *

from django.shortcuts import render
import csv

menu = [
    {'title': "Профиль", 'url_name': 'buildings'},
    {'title': "Выйти", 'url_name': 'login'},
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
            return HttpResponseRedirect(reverse_lazy('add_client'))
    else:
        form = AddClientForm()
    return render(request, 'buildings/adds/add_client.html', {'form': form, 'menu': menu, 'title': 'Добавление клиента'})

def add_deal(request):
    if request.method == 'POST':
        form = AddDealForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сделка успешно добавлена!')
            return HttpResponseRedirect(reverse_lazy('add_deal'))
    else:
        form = AddDealForm()
    return render(request, 'buildings/adds/add_deal.html', {'form': form, 'menu': menu, 'title': 'Добавление сделки'})

def add_contract(request):
    if request.method == 'POST':
        form = AddContractForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Контракт успешно добавлен!')
            return HttpResponseRedirect(reverse_lazy('add_contract'))
        else:
            print(form)
    else:
        form = AddContractForm()
    return render(request, 'buildings/adds/add_contract.html', {'form': form, 'menu': menu, 'title': 'Добавление договора'})

def get_buildings(request):
    model = Estate.objects.all()
    context = {
        'model': model,
        'menu': menu,
        'title': 'Все дома'
    }
    return render(request, 'buildings/estate.html', context = context)

def get_clients(request):
    model = Client.objects.all()
    context = {
        'model': model,
        'menu': menu,
        'title': 'Все клиенты'
    }
    return render(request, 'buildings/clients.html', context = context)

def get_employers(request):
    model = Employeers.objects.all()
    context = {
        'model': model,
        'menu': menu,
        'title': 'Все сотрудники'
    }
    return render(request, 'buildings/employers.html', context = context)

def get_deals(request):
    model = Deal.objects.all()
    context = {
        'model': model,
        'menu': menu,
        'title': 'Все сделки'
    }
    return render(request, 'buildings/deals.html', context = context)

def get_contracts(request):
    model = Contract.objects.all()
    context = {
        'model': model,
        'menu': menu,
        'title': 'Все договора'
    }
    return render(request, 'buildings/documents.html', context = context)

# def registration(CreateView):
#     form_class = UserCreationForm
#     template_name = 'buildings/registration_page.html'
#     success_url = (reverse_lazy('homepage'))

def import_csv_estate(request):
    response = HttpResponse(content_type='text/csv',headers={'Content-Disposition': 'attachment; filename="newfile.csv"'},)
    writer = csv.writer(response)
    estates = Estate.objects.all()
    writer.writerow(['ID', 'Адрес', 'Активное?', 'Тип объекта', 'Дата создания', 'Дата обновления'])

    for estate in estates:
        writer.writerow([estate.id_estate, estate.address, estate.active, estate.type_object, estate.time_create, estate.time_update])
    return response


def login(request):
    return render(request, 'buildings/registration_page.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
