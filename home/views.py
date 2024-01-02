from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import ContactForm
from .functions import *
from .tasks import *

def home(request):
    template_name = 'home.html'
    
    # test_func.delay()  # Celery

    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            first_name = contact_form.cleaned_data['first_name']
            last_name = contact_form.cleaned_data['last_name']
            org = contact_form.cleaned_data['org']
            email = contact_form.cleaned_data['email']
            comments = contact_form.cleaned_data['comment']
            subject = org
            from_mail = settings.EMAIL_HOST_USER
            body = {
		        'name': first_name+' '+last_name,
                'org': org,
		        'user_mail': email, 
		        'message': comments, 
		        }
            message = "\n".join(body.values())
            to_mail = [from_mail]
            result = send_mail_task.delay(subject, message, from_mail, to_mail)
            if result:
                # contact_form = ContactForm() # clear the form after sending mail
                return redirect('success_mail')
    context = {
        'contact_form':contact_form
    }
    return render(request, template_name, context)