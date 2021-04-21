import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BoboBlog.settings')

app = Celery('BoboBlog')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
