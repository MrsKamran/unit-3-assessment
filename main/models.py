from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse


class Task(models.Model):
    description = models.CharField(max_length=200)
    time = models.IntegerField(blank=True, null=True)
    person = models.CharField(max_length=100)

    def __str__(self):
        return self.description
   
    def get_absolute_url(self):
        return reverse('main:index')

        
