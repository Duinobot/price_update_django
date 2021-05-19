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
            n = 0
            for row in reader:
                # print(row[1])
                n = n+1
                product = Product.objects.create(
                    model=row[0],
                    name=row[1],
                    product_type=row[2],
                    cost=row[3],
                )
                print(n)
