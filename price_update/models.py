from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField

# Create your models here.


class Product(models.Model):

    class ProductType(models.TextChoices):
        Accessories = 'Accessories'
        Backs = 'Backs'
        Batteries = 'Batteries'
        Cables = 'Cables'
        Cases = 'Cases'
        Parts = 'Parts'
        Phones = 'Phones'
        Screens = 'Screens'
        Tempered_Glasses = 'Tempered_Glasses'
        Tools = 'Tools'
        Used = 'Used'

    model = models.IntegerField(blank=False, verbose_name="Model ID")
    name = models.CharField(blank=False, max_length=222,
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
    product_type = models.CharField(null=True, max_length=20,
                                    choices=ProductType.choices, verbose_name="Type")
    own_formula_regular = models.CharField(
        null=True, blank=True, max_length=100)
    own_formula_platinum = models.CharField(
        null=True, blank=True, max_length=100)
    own_formula_vvip = models.CharField(null=True, blank=True, max_length=100)
    own_formula_wholesale = models.CharField(
        null=True, blank=True, max_length=100)
    use_own_formula = models.BooleanField(default=False)
