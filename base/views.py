from django.shortcuts import render, redirect
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, "base/index.html")

def about(request):
    return render(request, "base/about.html")

def faqs(request):
    return render(request, "base/faqs.html")


def jobs(request):
    return render(request, "jobs/jobs.html")



def contact(request):
    if request.method == "POST":
        contact_name = request.POST.get('contactName')
        contact_email = request.POST.get('contactEmail')
        contact_message = request.POST.get('contactMessage')

        #send an email
        send_mail(
            contact_name, #subject
            contact_message, #message
            contact_email, #from email
            ['chrisneedham262@gmail.com'], #to email
        )
        
        return render(request, 'base/contact.html', {'contact_name': contact_name})
    else:

        return render(request, 'base/contact.html')


def insight(request):
    return render(request, "insight/insight.html")