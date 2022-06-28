from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [

    path("", views.OrderListView.as_view(), name="order_list"),

]
