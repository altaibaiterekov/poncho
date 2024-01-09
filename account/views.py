from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied

from rest_framework import viewsets

from account.serializers import RegisterSerializer, UserSerializer

User = get_user_model()


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer
        return UserSerializer
