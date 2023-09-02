from django.urls import re_path, include

from rest_framework.routers import DefaultRouter

from .views import *

app_name = "category"

router = DefaultRouter()

router.register(r"category", CategoryAPI, basename="category-app")

urlpatterns = [
    re_path(r"", include(router.urls)),
]
