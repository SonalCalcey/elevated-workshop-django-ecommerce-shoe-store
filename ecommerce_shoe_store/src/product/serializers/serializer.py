from product.models import Collection, Product, ProductVariant
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.fields import UUIDField, IntegerField, BooleanField, CharField, FloatField, SerializerMethodField


class CollectionSerializer(ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'

class ProductVariantSerializer(ModelSerializer):

    class Meta:
        model = ProductVariant
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    collection_id = serializers.CharField(source='collection.id')

    class Meta:
        model = Product
        exclude = ['collection', 'description']

class ProductDetailSerializer(ModelSerializer):
    collection = CollectionSerializer(read_only=True, required=False)
    product_variant = ProductVariantSerializer(read_only=True, required=False, many=True)

    class Meta:
        model = Product
        fields = '__all__'