from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

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

def sendEmail(request):

    if request.method == 'POST':

        template = render_to_string('base/email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['natanshost@gmail.com']
        )

        email.fail_silently=False
        email.send()
    return render(request, 'base/email_sent.html')