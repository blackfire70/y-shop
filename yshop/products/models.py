from django.db import models

# Create your models here.

class ProductCategory(models.Model):

    name = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=256, blank=True)
    slug = models.SlugField(max_length=256)
    price = models.DecimalField(max_digits=999999, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

    @property
    def img_urls(self):
        return [ product_img.image.urls for product_img in self.productimage_set.all() ]

    @property
    def main_image(self):
        
        all_img = self.productimage_set.filter(is_main=True)
        main_img = all_img.filter(is_main=True)
        return main_img[0] if main_img.exists() else all_img.first()


class ProductImage(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name