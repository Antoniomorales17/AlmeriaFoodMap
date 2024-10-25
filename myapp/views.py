from django.shortcuts import render, redirect  # Importa redirect aquí
from .models import Restaurant

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

def home(request):
    return redirect('restaurant_list')
