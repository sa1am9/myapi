from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings


class Account(AbstractBaseUser):

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    login_date = models.DateField(default=timezone.now)
    request_date = models.DateField(default=timezone.now)
    USERNAME_FIELD = 'id'

    def __str__(self):
        return self.username

