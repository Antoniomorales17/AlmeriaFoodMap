from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    
    # Definimos las opciones de categorías y el campo
    CATEGORY_CHOICES = [
        ('bar', 'Bar'),
        ('cafe', 'Café'),
        ('italiano', 'Italiano'),
        ('restaurante', 'Restaurante'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)  

    # Opciones de rango de precios y el campo
    PRICE_CHOICES = [
        ('€', 'Económico'),
        ('€€', 'Moderado'),
        ('€€€', 'Caro'),
    ]
    price_range = models.CharField(max_length=3, choices=PRICE_CHOICES, blank=True, null=True)  

    def __str__(self):
        return self.name
