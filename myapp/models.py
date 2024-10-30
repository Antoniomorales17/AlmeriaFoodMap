from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    CATEGORY_CHOICES = [
        ('bar', 'Bar'),
        ('cafe', 'Café'),
        ('italiano', 'Italiano'),
        ('restaurante', 'Restaurante'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)

    PRICE_CHOICES = [
        ('€', 'Económico'),
        ('€€', 'Moderado'),
        ('€€€', 'Caro'),
    ]
    price_range = models.CharField(max_length=3, choices=PRICE_CHOICES, blank=True, null=True)

    external_reviews_url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='reviews', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.rating} estrellas"
