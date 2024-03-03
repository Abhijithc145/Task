from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
app = Celery("src")

#we are using asia/kolkata time so we are making it False
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


#celery beat settings
app.conf.beat_schedule={
    'send-mail-everyday-at-11-45':{
        'task':'mailfireapp.tasks.send_mail_func',
        'schedule': crontab(hour=0,minute=2),
       
    }
}