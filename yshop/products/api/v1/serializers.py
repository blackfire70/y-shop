from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    photo_urls = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'description', 'slug', 'photo_urls']

    def get_photo_urls(self, obj):
        request = self.context.get('request')
        photos = obj.productimage_set.all()
        return [
            request.build_absolute_uri(photo.url)
            for photo in photos
        ]



