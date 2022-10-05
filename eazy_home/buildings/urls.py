from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('buildings/', get_buildings, name='buildings'),
    path('add_building/', add_estate, name='add_estate'),
    path('clients/', get_clients, name='clients'),
    path('employers/', get_employers, name='employers'),
    path('deals/', get_deals, name='deals'),
    path('contracts/', get_contracts, name='contracts'),
    path('add_client/', add_client, name='add_client'),
    path('add_deal/', add_deal, name='add_deal'),
    path('add_contract/', add_contract, name='add_contract'),
    path('import_csv_estate/', import_csv_estate, name='import_csv_estate'),
    # path('/buildings/<int:building_id/>', get_building)
]
