from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_home(request):
   return HttpResponse("<h1>Hello</h1>") 
    
def index(request):
    return HttpResponse("Helo this will be my blog at some point")

def create(request):
    return HttpResponse("Create")

def detail(request):
    return HttpResponse("Detail")

def list(request):
    return HttpResponse("List")

def update(request):
    return HttpResponse("Update")

def delete(request):
    return HttpResponse("Delete")
