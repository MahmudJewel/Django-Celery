from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse
from celery import shared_task

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


