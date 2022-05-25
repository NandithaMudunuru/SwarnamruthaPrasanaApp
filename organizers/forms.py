from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from faulthandler import disable
from .models import *

class OrganizerProfileUpdate(UserChangeForm): 
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )
        exclude = ('username', 'password', )

        
# Attendee Registration Form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'venue', 'start_time', 'end_time', 'Coordinator', 'eventStatus')
		labels = {
            'name': 'Name', 
            'venue': 'Venue', 
            'start_time': 'Event Start (time in 24hr format)', 
            'end_time': 'Event End (time in 24hr format)', 
            'Coordinator': 'Coordinator', 
            'eventStatus': 'Status',		
		}
		widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event name'}), 
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}), 
            'start_time': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD hh:mm:ss'}), 
            'end_time': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD hh:mm:ss'}), 
            'Coordinator': forms.Select(attrs={'class':'form-select'}), 
            'eventStatus': forms.Select(attrs={'class':'form-select'}),
		}