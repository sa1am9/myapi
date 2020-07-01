from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import UserManager

class Account(AbstractBaseUser):

    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    login_date = models.DateTimeField(default=timezone.now, blank=True)
    request_date = models.DateTimeField(default=timezone.now, blank=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'id'
    objects = UserManager()

    def __str__(self):
        return self.username

