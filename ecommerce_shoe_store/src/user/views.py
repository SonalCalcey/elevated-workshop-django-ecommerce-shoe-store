from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from common.middleware.exception_types import MethodNotImplementedException
from common.permissions.permissions import AllowAnyPermission
from user.models import Cart, CartItem
from user.serializers.serializer import UserSerializer, CartSerializer, CartItemSerializer, CartItemPostSerializer
import uuid

class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        raise MethodNotImplementedException()

    @action(detail=False, methods=['POST'], permission_classes=[AllowAnyPermission])
    def register(self, request):
        return super(UserViewSet, self).create(request)

class CartViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Cart.objects.prefetch_related('cart_item').all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = CartItem.objects.all()
    serializer_class = CartItemPostSerializer

    def create(self, request, user_id: int, cart_id: str, *args, **kwargs):
        if Cart.objects.filter(id=cart_id).first() is None:
            Cart.objects.create(user_id=user_id,id=cart_id)

        serializer = CartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['cart_id'] = cart_id

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)