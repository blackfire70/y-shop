from django.conf import settings
from rest_framework import serializers
from products.models import Product
from products.models import ProductCategory


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    product_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'slug', 'product_image_url']

    def get_product_image_url(self, obj):
        return f'{settings.SITE_URL}{obj.main_image.image.url}'

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


