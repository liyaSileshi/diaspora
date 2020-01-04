from django.db import models
from location_field.models.plain import PlainLocationField

class Event(models.Model):
    name = models.CharField(max_length=200)
    date_time = models.DateTimeField('event date time')
    street_address = models.CharField(max_length=255, default='address 1')
    city = models.CharField(max_length=255, default='city name')
    location = PlainLocationField(based_fields=['address','city'], zoom=7, default='location')
    description = models.TextField(default='description of the event')
    def __str__(self):
        return self.name