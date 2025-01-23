from django.db import models

class Events(models.Model):
    event_title = models.Charfield(max_length=100, blank=False)
    event_description = models.TextField()
    event_date_and_time = models.DateTimeField(auto_now_add=True, blank=False)
    event_location = models.CharField(max_length=100, blank=False)
    event_organizer = models.CharField(max_length=100)
    event_capacity = models.IntegerField() # maximum number of attendees


class Attendees(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

