from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    org = forms.CharField(required=False)
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()
