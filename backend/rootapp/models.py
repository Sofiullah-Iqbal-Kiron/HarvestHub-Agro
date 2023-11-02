from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    contact = models.CharField(verbose_name='primary contact number', max_length=11, unique=True) # BD specific number, primary
    location = models.TextField(verbose_name='full location or position of the user', null=True, blank=True)