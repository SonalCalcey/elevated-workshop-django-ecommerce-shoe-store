from django.contrib.auth.models import User
from django.db import models

from product.models import ProductVariant


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=False)

    class Meta:
        db_table = 'cart_item'
