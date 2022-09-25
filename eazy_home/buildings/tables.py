import django_tables2 as tables
from .models import *


class BuildingTable(tables.Table):
    class Meta:
        model = Building
        template_name = "buildings/index.html"
        fields = ('number', 'street', 'city', 'type_object', 'time_update')