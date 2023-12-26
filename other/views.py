from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

import random


class IndexView(View):
    def get(self, request):
        return render(request, 'other/index.html')


# Create your views here.
class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)


class ShowRandom(View):
    def get(self, request):
        my_num = random.randint(1, 5)
        return HttpResponse(my_num)

class ShowHello(View):
    def get(self, request):
        hello = "<h1>Hello, World</h1>"
        return HttpResponse(hello)

