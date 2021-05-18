from django.contrib import admin
from price_update.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'model', 'product_type')
    pass


admin.site.register(Product, ProductAdmin)
