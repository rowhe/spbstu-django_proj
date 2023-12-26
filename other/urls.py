from django.urls import path
from .views import IndexView, CurrentDateView, ShowRandom, ShowHello

urlpatterns = [
    path('datetime/', CurrentDateView.as_view()),
    path('random/', ShowRandom.as_view()),
    path('hello/', ShowHello.as_view()),
    path('', IndexView.as_view()),
]