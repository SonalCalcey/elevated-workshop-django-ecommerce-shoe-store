from django.contrib.auth.models import User
from django.db import models

from shoe.models import Shoe


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'
        constraints = [
            models.UniqueConstraint(fields=['user'], name='unique_user_constraint')
        ]


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)

    class Meta:
        db_table = 'cart_item'
