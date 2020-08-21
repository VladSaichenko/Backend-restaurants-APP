from rest_framework import viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from apps.users.serializers.serializers import RegistrationUserSerializer


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    """ Initilizing User and Token"""

    serializer_class = RegistrationUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = User(username=serializer.validated_data['username'])
        user.set_password(serializer.validated_data['password'])
        user.save()
        token = Token.objects.get_or_create(user=user)[0]

        return Response({'token': token.key, 'username': user.username}, status=status.HTTP_201_CREATED)
