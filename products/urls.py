from django.urls import re_path, include

from rest_framework.routers import DefaultRouter

from .views import *

app_name = "products"

router = DefaultRouter()

router.register(r"product", ProductAPI, basename="product-app")

urlpatterns = [
    re_path(r"", include(router.urls)),
]
