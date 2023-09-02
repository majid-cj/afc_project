from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from django.db import transaction
from django.views.decorators.csrf import csrf_exempt


from accounts.models import *
from accounts.serializers import *
from .serializers import *


class AFCProjectObtainToken(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = AFCProjectJWTSerializers


@permission_classes([AllowAny])
@csrf_exempt
@api_view(["post"])
@transaction.atomic
def SignupAPI(request):
    serializer = MemberSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data="account created", status=HTTP_201_CREATED)
