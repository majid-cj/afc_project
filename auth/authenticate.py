import jwt

from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class AFCProjectJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        User = get_user_model()
        authorization_heaader = request.headers.get("Authorization")

        if not authorization_heaader:
            return None

        try:
            access_token = authorization_heaader.split(" ")[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=["HS256"]
            )

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("access token expired")
        except IndexError:
            raise AuthenticationFailed("token prefix missing")

        user = User.objects.filter(id=payload["user_id"]).first()
        if user is None:
            raise AuthenticationFailed("user not found")

        if not user.is_active:
            raise AuthenticationFailed("user is inactive")

        return user, payload


class AuthUser(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(Q(email=email))
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

        return None
