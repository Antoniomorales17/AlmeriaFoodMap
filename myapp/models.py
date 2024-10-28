from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()

    # Imagen principal del restaurante
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)  # Cambiado de 'image' a 'main_image'

    # Opciones de categorías
    CATEGORY_CHOICES = [
        ('bar', 'Bar'),
        ('cafe', 'Café'),
        ('italiano', 'Italiano'),
        ('restaurante', 'Restaurante'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)

    # Opciones de rango de precios
    PRICE_CHOICES = [
        ('€', 'Económico'),
        ('€€', 'Moderado'),
        ('€€€', 'Caro'),
    ]
    price_range = models.CharField(max_length=3, choices=PRICE_CHOICES, blank=True, null=True)

    # Enlace a reseñas externas (como Google o TripAdvisor)
    external_reviews_url = models.URLField(blank=True, null=True)

    # Número de teléfono de contacto
    phone = models.CharField(max_length=15, blank=True, null=True)

    # Página web del restaurante
    website = models.URLField(blank=True, null=True)

    

    # Reseñas en texto
    reviews = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
