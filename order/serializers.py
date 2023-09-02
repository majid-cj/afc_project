from rest_framework import serializers
from .models import *


class OrderListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["pk", "product", "member", "status", "created_at"]


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["pk", "product", "member", "status"]
