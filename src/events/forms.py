from django import forms
from django.forms import ModelForm
from .models import Event, EventAttendance


#Form for adding events through site

class EventForm(ModelForm):
    
    class Meta:
        model = Event
        exclude = ["host"]
        fields = ('host', 'title', 'date', 'address', 'town', 'county', 'postcode', 'starttime', 'genre', 'description', 'price', 'duration')



class EventAttendanceForm(ModelForm):
	 
	 class Meta:
	 	model = EventAttendance
	 	exclude = ["person_key", "event_key"]
	 	fields = ['person_key', 'event_key']



        