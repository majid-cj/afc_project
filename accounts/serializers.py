from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from accounts.models import Member


class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["pk", "email", "name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return Member.objects.create_user(
            validated_data["name"], validated_data["email"], validated_data["password"]
        )


class MemberAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["pk", "email", "name"]
