from django.urls import path
from .views import Cart, Product, Shop

urlpatterns = [
    path('cart/', Cart.as_view()),
    path('product/', Product.as_view()),
    path('shop/', Shop.as_view()),
]