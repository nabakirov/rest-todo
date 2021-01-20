from rest_framework import serializers as s
from . import models
from rest_todo import exceptions


class UserSerializer(s.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'name', 'creation_date', 'last_login')
        read_only_fields = ('creation_date',)


class LoginSerializer(s.Serializer):
    username = s.CharField(max_length=200, required=True, allow_blank=False, allow_null=False)
    password = s.CharField(required=True, allow_blank=False, allow_null=False)


class RegistrationSerializer(s.Serializer):
    username = s.CharField(max_length=200, required=True, allow_blank=False, allow_null=False)
    name = s.CharField(max_length=200, required=False, allow_blank=False, allow_null=False)
    password = s.CharField(required=True, allow_blank=False, allow_null=False)

    def validate_username(self, value):
        try:
            models.User.objects.get_by_natural_key(value)
        except models.User.DoesNotExist:
            return value
        else:
            raise exceptions.UniqueError()
