from django.shortcuts import render, HttpResponse
lectures= [ 'TOA', 'DAA', 'AI', 'DM', 'DDMS']
# Create your views here.
def red(request):
    return render(request, "index.html",{'lec': lectures})
def olive(request):
    return render(request, "te.html")
