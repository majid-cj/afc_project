from django.urls import re_path, include

from rest_framework.routers import DefaultRouter

from .views import *

app_name = "order"

router = DefaultRouter()

router.register(r"order", OrderAPI, basename="order-app")

urlpatterns = [
    re_path(r"", include(router.urls)),
]
