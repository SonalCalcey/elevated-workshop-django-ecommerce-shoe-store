from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer
from product.models import Collection, Product
from product.serializers.serializer import ProductVariantSerializer, CollectionSerializer
from user.models import CartItem, Cart
from product.models import Product, ProductVariant

class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    collection = CollectionSerializer()

    class Meta:
        model = Product
        fields = '__all__'

class ProductVariantSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductVariant
        fields = '__all__'

class CartItemSerializer(ModelSerializer):
    product_variant = ProductVariantSerializer()
    quantity = IntegerField(required=True)

    class Meta:
        model = CartItem
        exclude = ['id', 'cart']

class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True, source='cart_item')

    class Meta:
        model = Cart
        exclude = ['id', 'user']
