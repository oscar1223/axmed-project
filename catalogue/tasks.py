from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_daily_email():
    subject = 'Informe Diario de SKUs'
    message = 'Este es un informe automático de los SKUs registrados en las últimas 24 horas.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['oscar@arauz.dev']
    send_mail(subject, message, from_email, recipient_list)