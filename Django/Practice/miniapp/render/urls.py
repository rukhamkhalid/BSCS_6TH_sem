from django.urls import path
from .import views
urlpatterns = [
    path("/ran",views.ran),
    path("/page",views.page)
]
