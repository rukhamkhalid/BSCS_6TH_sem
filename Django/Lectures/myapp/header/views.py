from django.shortcuts import render, HttpResponse
from django import forms

class Task(forms.Form):
    task= forms.CharField(label='task', max_length=64, min_length=5) 

# def index(request):
    # return render(request , 'index.html')
def about(request):
    return render(request , 'about.html')
def profiles(request):
    return render(request , 'profiles.html')
def courses(request):
    return render(request , 'courses.html')
def code(request):
    return render(request , 'code.html')
def task(request):
    return render(request , 'task.html')


# tasks=[]
# def home(request):
#     return render(request, '1home.html',{'task':tasks})
# def task(request):
    # if request.method=='POST':
    #     task=request.POST.get('task')
    #     tasks.append(task)
    #     return render(request, 'task.html',{'task':tasks})
    
    
    # if request.method=='POST':
    #     f=Task(request.POST)
    #     if f.is_valid():
    #         t=f.cleaned_data['task']
    #         tasks.append(t)
    #         return render(request,'task.html',{'task':tasks, 'form':Task()})
        
    #     return render(request, 'task.html',{'task':tasks, 'form':Task()})
    

    
# Create your views here.
def home(request):
    return render(request, '1home.html', {'task':request.session['tasks']})
def task(request):
    
 if request.method=='POST':
  f=Task(request.POST)
  if f.is_valid():
        t=f.cleaned_data['task']
        tasks=[]
        tasks=request.session['tasks']
        tasks.append(t)
        request.session['tasks']=tasks
        return render(request, 'task.html', {'task':request.session['tasks'], 'form':Task()})
 request.session['tasks']=list()
 return render(request, 'task.html', {'task':request.session['tasks'], 'form':Task()})
