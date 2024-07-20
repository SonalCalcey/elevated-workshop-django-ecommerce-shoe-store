from django.http import HttpResponse
from rest_framework import viewsets

class CollectionViewSet(viewsets.GenericViewSet):
    def list(self, request, *args, **kwargs):
        data = []
        return HttpResponse(content=data)

class ProductViewSet(viewsets.GenericViewSet):
    def retrieve(self, request, *args, **kwargs):
        data = {}
        return HttpResponse(content=data)
    def list(self, request, *args, **kwargs):
        data = []
        return HttpResponse(content=data)