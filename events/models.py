from django.db import models
# from location_field.models.plain import PlainLocationField

class Event(models.Model):
    name = models.CharField(max_length=200)
    date_time = models.DateTimeField('event date time')
    city = models.CharField(max_length=255)
    # location = PlainLocationField(based_fields=['city'], zoom=7)
