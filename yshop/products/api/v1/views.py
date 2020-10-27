from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from products.models import Product
from products.models import ProductCategory
from products.models import ProductImage
from products.api.v1.serializers import ProductCategorySerializer
from products.api.v1.serializers import ProductCategorySerializer
from products.api.v1.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer