from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('make_order', views.make_order, name="make_order"),
    path('warehouse', views.warehouse, name="warehouse"),
    path('orders/', views.orders, name="orders"),
    path('make_delivery', views.make_delivery, name="make_delivery"),
    path('make_product', views.make_product, name="make_product"),
    path('error', views.error, name="error"),
    path('make_pizza', views.make_pizza, name="make_pizza"),
    path('add_indigrient_to_pizza', views.add_indigrient_to_pizza, name="add_indigrient_to_pizza"),
    path('menu', views.menu, name="menu"),  
]
