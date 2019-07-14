from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.signup_view),
    path('login/',views.login_view),
]