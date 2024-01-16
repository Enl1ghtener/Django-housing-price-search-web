#coding=utf-8
from django.urls import path
from . import views


urlpatterns = [
    path('',views.search_view),
    path('search_results/<str:city_name>/', views.search_results, name='search_results')
]
