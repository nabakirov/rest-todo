from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_superuser(self, username, password):
        user = self.model(username=username, is_superuser=True)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password):
        user = self.model(username=username, is_superuser=False)
        user.set_password(password)
        user.save()
        return user

    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class User(AbstractBaseUser):
    class Meta:
        db_table = 'user'

    objects = UserManager()

    USERNAME_FIELD = 'username'
    username = models.CharField(_('username'), max_length=200, null=False, unique=True)
    name = models.CharField(_('name'), max_length=200, null=True)
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)

    is_superuser = models.BooleanField(_('is superuser'), null=False, default=False)
    is_active = models.BooleanField(_('is active'), null=False, default=True)

    def _update_last_login(self):
        # todo: move to background job
        self.last_login = timezone.now()
        self.save()

    def login(self):
        self._update_last_login()
        refresh = RefreshToken.for_user(self)
        return str(refresh), str(refresh.access_token)

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser

    def has_module_perms(self, *args, **kwargs):
        return self.is_active and self.is_superuser

    def has_perm(self, *args, **kwargs):
        return self.is_active and self.is_superuser
