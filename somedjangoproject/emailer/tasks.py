# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from celery import shared_task
from someproject import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from personsdata import persons

@shared_task(bind=True)
def send_emails(self):
    from_email = settings.EMAIL_HOST_USER
    
    for person in persons:
        subject = 'Письмо счастья'
        html_message = render_to_string(
            'emailer/letter.html', 
            {
                'first_name': person['first_name'],
                'surname': person['surname']
            }
        )
        plain_message = strip_tags(html_message)
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=from_email,
            recipient_list=[person['email']],
            html_message=html_message,
            fail_silently=True
            )
    return 'Sent'
    