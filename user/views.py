from rest_framework.viewsets import GenericViewSet, generics
from rest_framework.response import Response
from rest_framework import exceptions
from . import serializers as s
from . import models
from django.contrib.auth import authenticate


def get_login_response(user, request):
    refresh, access = user.login()
    data = {
        "user": s.UserSerializer(instance=user, context={'request': request}).data,
        "refresh": refresh,
        "access": access
    }
    return Response(data=data)


class LoginViewSet(generics.GenericAPIView):
    serializer_class = s.LoginSerializer
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(True)
        user = authenticate(request, **serializer.validated_data)
        if not user:
            raise exceptions.AuthenticationFailed()
        return get_login_response(user, request)


class RegistrationViewSet(generics.GenericAPIView):
    serializer_class = s.RegistrationSerializer
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(True)
        data = serializer.validated_data
        user = models.User(username=data['username'], name=data.get('name'))
        user.set_password(data['password'])
        user.save()
        return get_login_response(user, request)


class GetUserView(generics.GenericAPIView):
    serializer_class = s.UserSerializer
    pagination_class = None

    def get(self, request):
        return Response(data=self.get_serializer(instance=request.user).data)
