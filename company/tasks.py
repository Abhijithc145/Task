from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from src import settings
	
@shared_task(bind=True)
def send_mail_func(self,email,password):
    users=0
    
    if users==0:
        mail_subject="hello celery all"
        message=f"<p>Your password is: {password}</p><p>Regards,<br>ABCD Company</p>"
        to_email=email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
            )
    return "Task Successfull"