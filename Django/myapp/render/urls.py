from django.urls import path
from .import views
urlpatterns = [
    path("/red",views.red, name = 'index'),
    path("/olive",views.olive, name ='te')
    # path("/green",views.green),
    # path("/teal",views.teal),
    # path("/rust",views.rust)
]