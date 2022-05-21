from django import forms
from django.forms import ModelForm
from faulthandler import disable
from .models import *

# Attendee Registration Form
class AttendeeRegistrationForm(ModelForm):
	class Meta:
		model = Attendee
		fields = ('name', 'contact', 'ageOfParticipants')
		labels = {
			'name': 'Name',
			'contact': 'Phone Number',
			'ageOfParticipants': 'Age',			
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Surname     Given names'}),
			'contact': forms.TextInput(attrs={'class':'form-control', 'placeholder':'0000000000'}),
			'ageOfParticipants': forms.Select(attrs={'class':'form-select', 'placeholder':'1 - 16'}),
		}