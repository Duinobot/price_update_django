from django.contrib import admin
from django import forms
from django.forms.fields import FileField
from django.views.generic.base import RedirectView
from price_update.models import Product
from django.urls import path


class CsvImportForm(forms.Form):
    csv_file = FileField()


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

    # Add csv upload function
    change_list_template = 'price_update/product_changelist.html'

    def get_url(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_file']
            reader = csv.reader(csv_file)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "price_update/csv_form.html", payload
        )

    pass


# Register your models here.
admin.site.register(Product, ProductAdmin)
