from django.urls import path
from .views import MyLogin

urlpatterns = [
    path('login/', MyLogin.as_view()),
]