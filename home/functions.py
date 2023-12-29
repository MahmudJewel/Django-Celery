from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm

def sending_mail(contact_form):
    human = True
    # print('testing ============> ', contact_form.cleaned_data['first_name'])
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
    
    to_mail = [from_mail]
    message = "\n".join(body.values())
    try:
        print('ok mail ======')
        send_mail(subject, message, from_mail, [from_mail]) 
        # contact_form = ContactForm() # clear the form after sending mail
        # send_mail(subject, message, from_mail, [from_mail, 'bob@writing.fund'])
        return True 
    except BadHeaderError:
        # print('Mail error ========>', BadHeaderError)
        return HttpResponse('Invalid header found.')


