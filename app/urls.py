from django.urls import path
from .views import *

urlpatterns = [
    path('', list_cars, name='list'),
]