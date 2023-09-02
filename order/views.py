from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Order
from .serializers import OrderSerializers
from .paginations import OrderPaginationAPI


# Create your views here.
class OrderAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    pagination_class = OrderPaginationAPI
    serializer_class = OrderSerializers
    queryset = Order.objects.all().order_by("-created_at")
    filterset_fields = ["product", "member", "status"]
    search_fields = [
        "product__title",
        "product__product_category",
        "member__name",
        "member__email",
    ]
