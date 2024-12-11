from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_daily_email():
    subject = 'Daily SKUs Report'
    message = 'This is an automatic report of the SKUs registered in the last 24 hours.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['info@axmed.com']
    send_mail(subject, message, from_email, recipient_list)