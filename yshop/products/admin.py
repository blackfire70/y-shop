from django.contrib import admin
from products.models import Product
from products.models import ProductCategory
from products.models import ProductImage

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductImageAdmin(admin.ModelAdmin):
    pass

class ProductCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductImage, ProductImageAdmin)