from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'swapp'

urlpatterns = [
    path('', views.get_swapi, name='start'),
    path('category/<str:cat_name>/', views.get_swapi_category, name='category'),
]
