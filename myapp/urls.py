from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la raíz
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
]
