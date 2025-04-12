from django.urls import path
from .import views
urlpatterns = [
    path("/index",views.index, name = 'home'),
    path("/about",views.about, name = 'about'),
    path("/profiles",views.profiles, name ='profiles'),
    path("/code",views.code, name = 'code'),
    path("/courses",views.courses, name ='courses')
]