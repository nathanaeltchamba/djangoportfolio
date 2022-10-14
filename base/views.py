from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse

# Create your views here.

def home(request):
    return render(request, "base/homepage.html")
    
def profile(request):
    return render(request, "base/profile.html")

def about(request):
    return render(request, "base/about.html")

def contact(request):
    return render(request, "base/contact.html")

def view_pdf(request):
    try:
        return FileResponse(open('resume.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
