from django.shortcuts import render
from django.http import HttpResponse
from math import factorial
# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome To Views Of An APP</h1>")
def child(request):
    return render(request,"child.html")
def home(request):
    return render(request,"myapp1/home.html",{'name':"Akhil"})
def ak(request):
    return render(request,"myapp1/ak.html")