from django.urls import include, path

from rest_framework import routers

from products.api.v1.views import ProductCategoryViewSet
from products.api.v1.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product-categories', ProductCategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]