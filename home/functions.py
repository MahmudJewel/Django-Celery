from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse
from celery import shared_task
from django.conf import settings

@shared_task(bind=True)
def send_mail_task(self,subject, message, from_mail, to_mail):
    try:
        print('ok mail ======')
        send_mail(
            subject, 
            message, 
            from_mail, 
            to_mail, 
            fail_silently=True 
            ) 
        print('Mail send successfully =======>')
        return True 
    except BadHeaderError:
        # print('Mail error ========>', BadHeaderError)
        return HttpResponse('Invalid header found.')

@shared_task(bind=True)
def send_mail_automatically(self):
    try:
        subject = 'Mail from automatic'
        message = 'Lorem ipsum text from automatic'
        from_mail = settings.EMAIL_HOST_USER
        send_mail(
            subject, 
            message, 
            from_mail, 
            [from_mail], 
            fail_silently=True 
            ) 
    except BadHeaderError:
        # print('Mail error ========>', BadHeaderError)
        return HttpResponse('Invalid header found.')

