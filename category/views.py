from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category
from .serializers import CategorySerializers


# Create your views here.
class CategoryAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    serializer_class = CategorySerializers
    queryset = Category.objects.all().order_by("-category_name")
    filterset_fields = ["category_name"]
    search_fields = ["category_name"]
