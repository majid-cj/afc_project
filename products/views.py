from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductSerializers
from .paginations import ProductPaginationAPI


# Create your views here.
class ProductAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    pagination_class = ProductPaginationAPI
    serializer_class = ProductSerializers
    queryset = Product.objects.all().order_by("-created_at")
    filterset_fields = ["product_category"]
    search_fields = [
        "title",
        "product_category__category_name",
    ]
