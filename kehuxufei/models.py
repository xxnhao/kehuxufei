from django.db import models
from django.utils import timezone

# Create your models here.
class khxx(models.Model):
    kh_name = models.CharField(max_length=200)
    kh_url = models.CharField(max_length=200)
    kh_username = models.CharField(max_length=100)
    kh_password = models.CharField(max_length=100)
    kh_datetime = models.DateTimeField(default=timezone.now)
