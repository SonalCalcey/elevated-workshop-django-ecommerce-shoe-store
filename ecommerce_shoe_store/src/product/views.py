from rest_framework import viewsets, mixins

from common.responses.list.pagination import Pagination
from product.serializers.serializer import CollectionSerializer, ProductSerializer, ProductDetailSerializer
from product.models import Collection, Product
from rest_framework.response import Response

class CollectionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = Pagination

class ProductViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Product.objects.prefetch_related('product_variant').all()
    pagination_class = Pagination

    def get_serializer_class(self):
        match self.action:
            case 'retrieve':
                return ProductDetailSerializer
            case _:
                return ProductSerializer
