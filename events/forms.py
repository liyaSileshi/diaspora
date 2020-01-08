from django import forms
from events.models import Event
from location_field.forms.plain import PlainLocationField

class EventForm(forms.ModelForm):
    """ Render and process a form based on the Event model. """
    class Meta:
        model = Event
        fields = [
                'name',
                'date_time', 
                'street_address',
                'city',
                'location',
                'description'
            ]

