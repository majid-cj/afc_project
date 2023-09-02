from rest_framework import serializers
from .models import *


class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "pk",
            "product_category",
            "title",
            "description",
            "product_image",
            "created_at",
        ]


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["pk", "product_category", "title", "description", "product_image"]
