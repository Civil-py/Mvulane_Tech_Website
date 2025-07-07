from django.urls import path
from . import views


urlpatterns = [

    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("espanini", views.espanini, name="espanini"),
    path("Website-Development", views.webdev, name="webdev"),

]



