from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer
from product.models import Collection, Product
from product.serializers.serializer import ProductVariantSerializer
from user.models import CartItem, Cart


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

class CartItemsSerializer(ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'

class CartItemSerializer(ModelSerializer):
    product_variant_id = IntegerField(required=True)
    quantity = IntegerField(required=True)

    class Meta:
        model = CartItem
        exclude = ['id', 'cart', 'product_variant']

class CartSerializer(ModelSerializer):
    cart_item = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'
