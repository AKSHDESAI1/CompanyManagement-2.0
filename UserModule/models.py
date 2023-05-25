from django.db import models
from django.contrib.auth.models import AbstractUser, User

# # Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_owner = models.BooleanField('Is owner', default=False)
    is_manager = models.BooleanField('Is manager', default=False)
    is_supervisor = models.BooleanField('Is supervisor', default=False)
    is_assistant = models.BooleanField('Is assistant', default=False)


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    dbaName = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    branch = models.CharField(max_length=70)
    number = models.BigIntegerField()
    website = models.CharField(max_length=70)
    fax = models.CharField(max_length=70)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=70)
    manager = models.CharField(max_length=70)
    supervisor = models.CharField(max_length=70)
    assistants = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=70)
    manager = models.CharField(max_length=70)
    supervisor = models.CharField(max_length=70)
    assistants = models.CharField(max_length=70)

    def __str__(self):
        return self.name
