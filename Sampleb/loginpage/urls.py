from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainpage, name = "mainpage"),
    path('', views.login, name = "login"),
]