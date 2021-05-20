import csv
from os import confstr

from django.core.management.base import BaseCommand, CommandError
from price_update.models import Product

# python manage.py import-products --path file.csv


class Command(BaseCommand):
    help = 'import product from csv files'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')

            # Determine if there's header, skip head if so
            header = next(reader)

            n = 0
            for row in reader:
                # print(row[1])
                n = n+1
                print(n)

                try:
                    product, created = Product.objects.get_or_create(
                        model=row[0], name=row[1], product_type=row[2], cost=row[3],
                    )
                except:
                    print(f"error in row {n}")
                    continue
