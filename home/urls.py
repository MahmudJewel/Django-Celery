from django.urls import path, include
from django.views.generic import TemplateView
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('success-mail', TemplateView.as_view(template_name='feedback/success_mail.html'), name='success_mail'),
] 