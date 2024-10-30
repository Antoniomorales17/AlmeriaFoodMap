import requests  # Necesario para realizar solicitudes a la API de Google
from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant
from .forms import ReviewForm


# Función para obtener las coordenadas usando la API de Google Places y guardar en la base de datos
def obtener_coordenadas_y_guardar(nombre):
    api_key = 'AIzaSyAyFv6Ofl9Wx2S3kuc1oXaKfNMS6aPpu5E'  # Reemplaza con tu clave API de Google Places
    url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={nombre}&inputtype=textquery&fields=name,geometry&key={api_key}'

    response = requests.get(url)
    data = response.json()

    if data.get('candidates'):
        bar_info = data['candidates'][0]
        latitude = bar_info['geometry']['location']['lat']
        longitude = bar_info['geometry']['location']['lng']

        # Guardar el restaurante en la base de datos
        Restaurant.objects.create(
            name=nombre,
            latitude=latitude,
            longitude=longitude,
        )
        return True  # Se guardó correctamente
    return False  # No se encontró el lugar

# Vista para la lista de restaurantes
def restaurant_list(request):
    # Obtenemos todos los restaurantes de la base de datos
    restaurants = Restaurant.objects.all()
    
    # Renderizamos la plantilla y enviamos los restaurantes y las coordenadas de la ciudad
    return render(request, 'restaurant_list.html', {
        'restaurants': restaurants,
        'ciudad': {'lat': 36.8340, 'lng': -2.4637}  # Coordenadas de Almería
    })

# Vista principal que redirige a la lista de restaurantes
def home(request):
    return redirect('restaurant_list')  # Redirige a la lista de restaurantes

# Vista para agregar un bar y buscar sus coordenadas automáticamente

def agregar_bar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        
        # Llama a la función para obtener coordenadas y guardar en la base de datos
        if obtener_coordenadas_y_guardar(nombre):
            return redirect('restaurant_list')  # Redirige a la lista de restaurantes si se guarda
        else:
            # Si no se encontró el bar, maneja el error
            return render(request, 'error.html', {'message': 'No se encontró el lugar.'})
    
    return render(request, 'agregar_bar.html')

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.reviews.all()  # Obtiene todas las reseñas para el restaurante
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant  # Asocia la reseña al restaurante actual
            review.save()
            return redirect('restaurant_detail', restaurant_id=restaurant.id)
    else:
        form = ReviewForm()
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'reviews': reviews,
        'form': form
    })