from django.db import models
from django.utils import timezone
from account.models import Account

class Post(models.Model):

    text  = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)

    date = models.DateField(default=timezone.now)
    count_like = models.IntegerField(default=0)
    count_unlike = models.IntegerField(default=0)

    def __str__(self):
        return self.text



