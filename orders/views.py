from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.base import View
from .filters import OrderFilter
from .models import Order


class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = OrderFilter(self.request.GET, queryset=Order.objects.order_by('id'))
        return context





