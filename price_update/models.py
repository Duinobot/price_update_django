from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField

# Create your models here.


class Product(models.Model):

    class ProductType(models.IntegerChoices):
        Accessories = 1
        Backs = 2
        Batteries = 3
        Cables = 4
        Cases = 5
        Parts = 6
        Phones = 7
        Screens = 8
        Tempered_Glasses = 9
        Tools = 10
        Used = 11

    model = models.IntegerField(blank=False, verbose_name="Model ID")
    name = models.CharField(blank=False, max_length=100,
                            verbose_name="Product Name")
    cost = models.DecimalField(null=True,
        blank=True, max_digits=6, decimal_places=2, verbose_name="Cost")
    price_regular = models.DecimalField(null=True,
        blank=True, max_digits=6, decimal_places=2)
    price_platinum = models.DecimalField(null=True,
        blank=True, max_digits=6, decimal_places=2)
    price_vvip = models.DecimalField(null=True,
        blank=True, max_digits=6, decimal_places=2)
    price_wholesale = models.DecimalField(null=True,
        blank=True, max_digits=6, decimal_places=2)
    product_type = models.IntegerField(null=True,
        choices=ProductType.choices, verbose_name="Type")
    own_formula_regular = models.CharField(null=True, blank=True, max_length=100)
    own_formula_platinum = models.CharField(null=True, blank=True, max_length=100)
    own_formula_vvip = models.CharField(null=True, blank=True, max_length=100)
    own_formula_wholesale = models.CharField(null=True, blank=True, max_length=100)
    use_own_formula = models.BooleanField(default=False)
