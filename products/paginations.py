from rest_framework.pagination import PageNumberPagination


class ProductPaginationAPI(PageNumberPagination):
    page_size = 15
