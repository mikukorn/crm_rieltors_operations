from django.urls import path
from .views import *

urlpatterns = [
    path('', get_buildings, name='buildings'),
    path('add_building/', add_building, name='add_building'),
    # path('/buildings/<int:building_id/>', get_building)
]
