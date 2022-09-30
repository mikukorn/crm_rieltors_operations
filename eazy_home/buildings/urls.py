from django.urls import path
from .views import *

urlpatterns = [
    path('', get_buildings, name='buildings'),
    path('add_building/', add_estate, name='add_estate'),
    path('add_client/', add_client, name='add_client'),
    # path('/buildings/<int:building_id/>', get_building)
]
