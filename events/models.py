from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.TextField()
    event_date = models.DateField()
    organizer = models.TextField()
    is_active = models.BooleanField()