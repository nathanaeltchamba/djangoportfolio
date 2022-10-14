from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h2>Home Page</h2>")
    
def profile(request):
    return HttpResponse("<h2>Profile Page</h2>")

def about(request):
    return HttpResponse("<h2>About Page</h2>")

def contact(request):
    return HttpResponse("<h2>Contact Page</h2>")

