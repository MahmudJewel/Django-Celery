# django_celery/celery.py
from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Dhaka')

app.config_from_object("django.conf:settings", namespace="CELERY")

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-30': {
        'task': 'home.functions.send_mail_automatically',
        'schedule': crontab(minute='*/5'),
        #'args': (2,)
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
