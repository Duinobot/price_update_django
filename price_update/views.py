from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product
from django.views.generic import ListView


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('model')
    serializer_class = ProductSerializer


class ProductPageView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'all_product_list'
