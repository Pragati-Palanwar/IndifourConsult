from django.urls import path

from . import views

urlpatterns = [
    path("api1", views.listofcountries, name="listofcountries"),
    path("api2/<countryCode>", views.populationyear, name="populationyear"),
    path("api3/<temperature>", views.tempconvert, name="tempconvert"),
]