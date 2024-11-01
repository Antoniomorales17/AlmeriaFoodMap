# Generated by Django 5.1.2 on 2024-10-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_restaurant_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='external_reviews_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant_photos/'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='reviews',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
