# Generated by Django 5.1.2 on 2024-10-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_restaurant_category_restaurant_price_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.CharField(blank=True, choices=[('bar', 'Bar'), ('cafe', 'Café'), ('italiano', 'Italiano'), ('restaurante', 'Restaurante')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='price_range',
            field=models.CharField(blank=True, choices=[('€', 'Económico'), ('€€', 'Moderado'), ('€€€', 'Caro')], max_length=3, null=True),
        ),
    ]