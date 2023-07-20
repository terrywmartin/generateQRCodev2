from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings


#from core.utils import email_user
from core.tasks import email_user, email_user_sync

import uuid

from core.storage_backends import PublicMediaStorage

# Create your models here.
class User(AbstractUser):
   
   id = models.UUIDField(primary_key=True,null=False,blank=False,default=uuid.uuid4)

   def send_activation(self):
      
      html = render_to_string('emails/activate_user.html', {
         'user': self.first_name,
         'domain': settings.APP_URL,
         'app_name': settings.APP_NAME,
         'uid': urlsafe_base64_encode(force_bytes(self.id)),
         'token': default_token_generator.make_token(self),
         'debug': settings.DEBUG,
      })
      
      #response = email_user.delay(self.email, html, subject="Activate account")
      response = email_user_sync(self.email, html, subject="Activate account")

   def send_password_reset(self):
      
      html = render_to_string('emails/reset_password.html', {
         'user': self.first_name,
         'domain': settings.APP_URL,
         'app_name': settings.APP_NAME,
         'uid': urlsafe_base64_encode(force_bytes(self.id)),
         'token': default_token_generator.make_token(self),
      })
      
      response = email_user.delay(self.email, html, subject='Reset Password')
      

class UserProfile(models.Model):
   id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
   
   user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE, null=True, blank=True)

   def __str__(self):
        return str(self.user.username)
