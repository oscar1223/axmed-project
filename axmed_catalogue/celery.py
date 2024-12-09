import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'axmed_catalogue.settings')

app = Celery('axmed_catalogue')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()