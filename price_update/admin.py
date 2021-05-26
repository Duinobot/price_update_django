from django.contrib import admin
from price_update.models import Product
from import_export import resources

# Create Import Export Resource
class ProductResource(resources.ModelResource):
    
    class Meta:
        model = Product
        fields = ("model", "name", "cost",)


# Register your models here.
class ProductAdmin(admin.ModelAdmin):

    # Add Calculated field Change % in product detail field
    readonly_fields = ('change_percentage',)

    # Use admin.display decorator to calculate cost change %
    @admin.display(description='Change %')
    def change_percentage(self, obj):
        if obj.new_cost and obj.cost:
            change_percentage = (obj.new_cost - obj.cost) / obj.cost
            return "{0:.0%}".format(change_percentage)

    list_display = ['name', 'cost', 'new_cost', 'change_percentage', 'model',
                    'product_type', ]

    search_fields = ['name', 'model']
    list_filter = ['product_type', 'use_own_formula']

    fieldsets = [
        ('Product Info', {'fields': [
         ('model', 'product_type'), 'name', ('cost', 'new_cost', 'change_percentage')]}),
        ('Price', {'fields': [
         'price_regular', 'price_platinum', 'price_vvip', 'price_wholesale']}),
        ('Formula', {'fields': [
         'use_own_formula', 'own_formula_regular', 'own_formula_platinum', 'own_formula_vvip', 'own_formula_wholesale']}),
    ]
    pass


admin.site.register(Product, ProductAdmin)
