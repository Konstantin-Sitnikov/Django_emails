from django.core.mail import mail_managers
from django_apscheduler.models import DjangoJobExecution

# наша задача по выводу текста на экран
def my_job():
    #  Your job processing logic here...
    print('hello from job')

# функция, которая будет удалять неактуальные задачи
def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)



def send_mail():
    mail_managers(
        subject='Письмо от django',
        message='Сообщение от django'
    )