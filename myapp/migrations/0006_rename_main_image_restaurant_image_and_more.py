# Generated by Django 5.1.2 on 2024-10-28 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_photo_restaurant_secondary_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='main_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='secondary_image',
        ),
    ]