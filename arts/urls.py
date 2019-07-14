from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create_art/',views.create_art),
    path('home/',views.art_view),
     path('detail/<int:id>',views.detail_art),
]