from rest_framework.filters import OrderingFilter
from rest_framework import permissions, generics
from orders.models import Order
from .pagination import CustomPageNumberPagination
from .serializers import ListOrderSerializer


class OrderListView(generics.ListAPIView):
    """Список избранных постов
    """
    pagination_class = CustomPageNumberPagination
    serializer_class = ListOrderSerializer
    filter_backends = [OrderingFilter]
    permission_classes = [permissions.AllowAny]
    ordering_fields = ['dol_price', 'rub_price']
    queryset = Order.objects.all()

