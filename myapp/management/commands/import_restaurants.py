import csv
from django.core.management.base import BaseCommand
from myapp.models import Restaurant


class Command(BaseCommand):
    help = 'Importa restaurantes desde un archivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file'], newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                Restaurant.objects.create(
                    name=row['name'],
                    address=row['address'],
                    latitude=row['latitude'],
                    longitude=row['longitude'],
                    category=row.get('category', ''),
                    price_range=row.get('price_range', ''),
                    description=row.get('description', ''),
                    opening_time=row.get('opening_time', '09:00'),
                    closing_time=row.get('closing_time', '23:00'),
                    phone=row.get('phone', ''),
                    website=row.get('website', ''),
                )
                count += 1
            self.stdout.write(f'Importados {count} restaurantes')
