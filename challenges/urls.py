from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.montlyChallengeNumber),
    path("<str:month>", views.monthlyChallenge, name="month-challenge"),
]