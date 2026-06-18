from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
]

# Configuración para servir archivos multimedia en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
