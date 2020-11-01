from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("mobile", views.mobile, name="mobile"),
    path("laptop", views.laptop, name="laptop"),
    path("other", views.other, name="other"),
    path("older", views.older, name="older"),
    path("Home", views.Home, name="Home"),
    path("contact", views.contact, name="contact"),
]