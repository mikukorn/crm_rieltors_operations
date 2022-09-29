from django.contrib import admin
from django.urls import path, include

from buildings.views import *
from homepage.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('buildings/', include('buildings.urls')),
    # path('realtors/', include('realtors.urls')),
    # path('documents/', include('documents.urls')),
]

