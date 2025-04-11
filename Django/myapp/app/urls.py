from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/ptanahi',views.a),
    path('/b',views.b),
    path('/c',views.c),
    path('/d',views.d),
    path('/e',views.e),
    path('/f',views.f)
]