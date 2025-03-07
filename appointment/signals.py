from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import mail_managers

from .models import Appointment



@receiver(post_save, sender=Appointment)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.client_name} {instance.date.strftime("%d %m %Y")}'
    else:
        subject = f'Appointment changed for {instance.client_name} {instance.date.strftime("%d %m %Y")}'

    mail_managers(
        subject=subject,
        message=instance.message,
    )


@receiver(post_delete, sender=Appointment)
def notify_managers_appointment(sender, instance, **kwargs):

    subject = f'{instance.client_name} отменил запись'

    mail_managers(
        subject=subject,
        message=f'запись клиента {instance.client_name} на {instance.date.strftime("%d %m %Y")} была отменена!',
    )


