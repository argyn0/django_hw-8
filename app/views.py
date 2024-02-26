from django.shortcuts import render
from .models import Car

def list_cars(request):  
    cars = Car.objects.all()
    return render(request, 'list_cars.html', {'cars': cars})

def create_car(request):
    return render(request, 'create_car.html')