from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from celery import shared_task
from .forms import ContactForm

@shared_task(bind=True)
def send_mail_task(self,subject, body):
    from_mail = settings.EMAIL_HOST_USER
    message = "\n".join(body.values())
    try:
        print('ok mail ======')
        send_mail(subject, message, from_mail, [from_mail]) 
        # contact_form = ContactForm() # clear the form after sending mail
        # send_mail(subject, message, from_mail, [from_mail, 'bob@writing.fund'])
        print('Mail send successfully =======>')
        return True 
    except BadHeaderError:
        # print('Mail error ========>', BadHeaderError)
        return HttpResponse('Invalid header found.')


