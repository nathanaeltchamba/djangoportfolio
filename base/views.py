from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse

# Create your views here.

def home(request):
    return render(request, "base/homepage.html")

def view_resume(request):
    try:
        return FileResponse(open('resume.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def view_crm(request):
    try:
        return FileResponse(open('crm.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def view_discord(request):
    try:
        return FileResponse(open('discord_clone.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def view_real_estate(request):
    try:
        return FileResponse(open('real_estate.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
