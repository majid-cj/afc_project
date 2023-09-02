from django.urls import re_path

from .views import *


app_name = "auth"

urlpatterns = [
    re_path(r"sign-in/", AFCProjectObtainToken.as_view(), name="sign_in"),
    re_path(r"sign-up/", SignupAPI),
]
