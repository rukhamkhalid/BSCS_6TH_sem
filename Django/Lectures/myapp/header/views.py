from django.shortcuts import render, HttpResponse

def index(request):
    return render(request , 'index.html')
def about(request):
    return render(request , 'about.html')
def profiles(request):
    return render(request , 'profiles.html')
def courses(request):
    return render(request , 'courses.html')
def code(request):
    return render(request , 'code.html')


# Create your views here.
