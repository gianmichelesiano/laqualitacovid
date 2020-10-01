from django.conf import settings 
from django.db import models 
from django.utils import timezone 


class SimpleForm(models.Model):
     Vorname = models.CharField(max_length=200, blank=False)
     Familienname = models.CharField(max_length=200, blank=False)
     Telefonnummer = models.CharField(max_length=200, blank=False)
     Zustimmung = models.BooleanField(default=True)
     created_date = models.DateTimeField(default=timezone.now)

