from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

from rest_framework_simplejwt.tokens import AccessToken

from django.shortcuts import reverse
from .managers import MemberManager


# Create your models here.


class Member(PermissionsMixin, AbstractBaseUser):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = ["name", "password"]
    USERNAME_FIELD = "email"

    objects = MemberManager()

    def __str__(self):
        return f"{self.name} - {str(object=self.email)}"

    def natural_key(self):
        return self.name

    def get_auth_token(self):
        return AccessToken.for_user(user=self)

    def check_is_superuser(self):
        return self.is_superuser
