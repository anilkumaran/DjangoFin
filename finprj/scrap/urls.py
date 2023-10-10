from django.urls import path

from . import views

urlpatterns = [
    path("laptops", views.get_laptops, name="get_laptops"),
]