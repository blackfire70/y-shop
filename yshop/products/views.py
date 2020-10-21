from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product
from products.models import ProductCategory


class ProductListView(TemplateView):
    template_name = "index.html"


    def get_context_data(self):
        context_data = super().get_context_data()
        context_data['products'] = Product.objects.all()
        context_data['product_cats'] = ProductCategory.objects.all()

        return context_data