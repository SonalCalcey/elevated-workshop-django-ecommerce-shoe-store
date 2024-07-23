from rest_framework import viewsets, mixins

from common.responses.list.pagination import Pagination
from product.serializers.serializer import CollectionSerializer, ProductSerializer, ProductDetailSerializer
from product.models import Collection, Product

class CollectionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class ProductViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Product.objects.prefetch_related('product_variant').all()
    pagination_class = Pagination

    def get_queryset(self):
        if self.action == 'list':
            collection_id = self.request.query_params.get("collection_id", None)
            if collection_id:
                return Product.objects.filter(collection_id=collection_id)

        return super().get_queryset()

    def get_serializer_class(self):
        match self.action:
            case 'retrieve':
                return ProductDetailSerializer
            case _:
                return ProductSerializer
