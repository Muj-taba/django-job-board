from django.shortcuts import render
from .models import Info
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.

def send_message(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
       
        name = request.POST['name']
        subject = request.POST['message']
        email   = request.POST['email']
        message = request.POST['subject']
        send_mail(
            name,
            subject,
            message,
           [settings.EMAIL_HOST_USER],
            email,
            

        )

    return render(request, 'contact/contact.html',{'myinfo':myinfo})