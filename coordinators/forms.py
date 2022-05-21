from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from faulthandler import disable
from .models import *

# Attendee Registration Form
class AttendeeApprovalForm(ModelForm):
	class Meta:
		model = Attendee
		fields = ('event', 'name', 'contact', 'ageOfParticipants')
		labels = {
            'event': 'Event',
			'name': 'Name',
			'contact': 'Phone Number',
			'ageOfParticipants': 'Age',			
		}
		widgets = {
			'event': forms.Select(attrs={'class':'form-select', 'placeholder':'Event'}),
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Surname     Given names'}),
			'contact': forms.TextInput(attrs={'class':'form-control', 'placeholder':'0000000000'}),
			'ageOfParticipants': forms.Select(attrs={'class':'form-select', 'placeholder':'1 - 16'}),
		}

class CoordinatorProfileUpdate(UserChangeForm): 
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )
        exclude = ('username', 'password', )