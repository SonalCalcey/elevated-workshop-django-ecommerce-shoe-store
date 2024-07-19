from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from common.middleware.exception_types import MethodNotImplementedException
from common.permissions.permissions import AllowAnyPermission
from user.serializers.serializer import UserSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        raise MethodNotImplementedException()

    @action(detail=False, methods=['POST'], permission_classes=[AllowAnyPermission])
    def register(self, request):
        return super(UserViewSet, self).create(request)
