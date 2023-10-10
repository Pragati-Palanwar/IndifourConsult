from django.urls import path

from . import views

urlpatterns = [
    path("api1", views.index, name="index"),
    path("api2/<countryCode>", views.index2, name="index2"),
    path("api3", views.index3, name="index3"),
]