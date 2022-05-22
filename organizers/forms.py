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