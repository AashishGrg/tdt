from templated_email import send_templated_mail
from django.core.mail import get_connection
from dashboard.models import EmailConfig
import threading
from random import randint


class mailThread(threading.Thread):

    def __init__(self, from_e, tolist, message, template, contexts):
        threading.Thread.__init__(self)
        self.threadID = randint(1000, 99999)
        self.name = 'Thread' + str(self.threadID)
        self.counter = 1
        self.from_e = from_e
        self.tolist = tolist
        self.message = message
        self.template = template
        self.contexts = contexts
        self.setDaemon(True)

    def run(self):
        mail(self.from_e, self.tolist, self.message,
             self.template,  self.contexts)


def mail(from_e, tolist, message, template, contexts):
    configs = EmailConfig.objects.filter(default=True)
    if configs.count() > 0:
        conf = configs.first()
        from django.conf import settings
        settings.DEFAULT_FROM_EMAIL = conf.default_from_email
        settings.EMAIL_HOST = conf.email_host
        settings.EMAIL_HOST_USER = conf.email_host_user
        settings.EMAIL_HOST_PASSWORD = conf.email_host_password
        settings.EMAIL_PORT = conf.email_port
        settings.EMAIL_USE_TLS = conf.email_use_tls
        send_templated_mail(
            template_name=template,
            from_email=from_e,
            recipient_list=tolist,
            context=contexts,
            fail_silently=False,
        )
    else:
        from django.conf import settings
        settings.DEFAULT_FROM_EMAIL = "shekhar.rai.2053@gmail.com"
        settings.EMAIL_HOST = "smtp.gmail.com"
        settings.EMAIL_HOST_USER = "shekhar.rai.2053@gmail.com"
        settings.EMAIL_HOST_PASSWORD = "Shekkkkar1997"
        settings.EMAIL_PORT = 587
        settings.EMAIL_USE_TLS = True
        send_templated_mail(
            template_name=template,
            from_email=from_e,
            recipient_list=tolist,
            context=contexts,
            fail_silently=False,
        )
