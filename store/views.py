from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.

class Cart(View):
    def get(self, request):
        return render(request, 'store/cart.html')


class Product(View):
    def get(self, request):
        return render(request, 'store/product-single.html')

class Shop(View):
    def get(self, request):
        return render(request, 'store/shop.html')
