from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm
from .functions import *

def home(request):
    template_name = 'home.html'
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            result = sending_mail(contact_form)
            if result:
                # contact_form = ContactForm() # clear the form after sending mail
                return redirect('success_mail')
    context = {
        'contact_form':contact_form
    }
    return render(request, template_name, context)