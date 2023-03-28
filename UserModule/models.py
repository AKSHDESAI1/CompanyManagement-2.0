from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_manager = models.BooleanField('Is manager', default=False)
    is_supervisor = models.BooleanField('Is supervisor', default=False)
    is_assistant = models.BooleanField('Is assistant', default=False)
