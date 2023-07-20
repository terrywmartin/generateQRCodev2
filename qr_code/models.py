from django.db import models

import uuid

from users.models import User

# Create your models here.
class QRCode(models.Model):
    id = models.UUIDField(primary_key=True,null=False,default=uuid.uuid4,blank=False)

    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(blank=False,null=False)

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

