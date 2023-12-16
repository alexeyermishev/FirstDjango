from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from MainApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path("item/<int:id>/", views.get_item, name='item'),
    path("items", views.get_items, name='itemslist'),
]
