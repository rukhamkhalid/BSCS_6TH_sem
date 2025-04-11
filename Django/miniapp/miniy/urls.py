from django.urls import path
from .import views

urlpatterns = [
    path('/i', views.i, name ='i'),
    path('/j', views.j ),
    path('/k', views.k ),
    path('/l', views.l ),
    path('/m', views.m ),
    
]
