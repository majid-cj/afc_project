from accounts.serializers import MemberSerializers
from auth.authenticate import AuthUser

from django.contrib.auth.models import update_last_login
from django.db import transaction


from rest_framework import exceptions

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AFCProjectJWTSerializers(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    @transaction.atomic
    def validate(self, attrs):
        email = attrs.get("email", None)
        password = attrs.get("password", None)
        user = AuthUser().authenticate(email=email, password=password)

        if not user:
            raise exceptions.AuthenticationFailed()

        refresh = self.get_token(user)

        data = {}

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["user"] = MemberSerializers(user).data if user else None

        update_last_login(None, user)

        return data
