from django.shortcuts import render, HttpResponse

result=['1st','2nd','3rd','4th']     

def ran(request):
    return render(request,"i.html",{'res':result})
def page(request):
    return render(request,"n.html")   
# Create your views here.
