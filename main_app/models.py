from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField('event date')
    time = models.TimeField()
    event_details = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('event_details', kwargs={'pk': self.id})

