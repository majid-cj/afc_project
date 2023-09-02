from rest_framework.pagination import PageNumberPagination


class OrderPaginationAPI(PageNumberPagination):
    page_size = 15
