from django.http import HttpResponse
from django.shortcuts import render
def py(request):
    return HttpResponse("Normal Http Response from py file")
def index(request):
    return render(request,"myapp/index.html")
def about(request):
    return render(request,"myapp/about.html")

