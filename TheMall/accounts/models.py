from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    full_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL)
    # username/email/password come from AbstractUser
