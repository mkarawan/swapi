from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'swapp'

urlpatterns = [
    path('', views.get_swapi, name='start'),
    path('category/<str:cat_name>/', views.get_swapi_category, name='category'),
    path('category/<str:cat_name>/<int:url_number>', views.get_swapi_details, name='details'),
]
