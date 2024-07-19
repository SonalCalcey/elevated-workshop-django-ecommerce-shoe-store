from django.db import models


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'collection'


class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    image_url = models.CharField(null=True)
    price = models.FloatField(null=False)
    description = models.CharField(max_length=300, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

    class Meta:
        db_table = 'product'


class ProductVariant(models.Model):
    variant = models.CharField(max_length=50, null=False)
    stock = models.IntegerField(null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_variant'
