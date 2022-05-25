from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField('Venue Address', max_length=400)
    pincode = models.CharField('Venue Post Code', max_length=10)
    web = models.URLField('Venue Website', max_length=120, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.PROTECT)
    get_now = datetime.now()
    start_time = models.DateTimeField(default=get_now.strftime("%Y-%m-%d %H:%M"))
    end_time = models.DateTimeField(default=(get_now+ timedelta(hours=1)).strftime("%Y-%m-%d %H:%M"))
    Coordinator = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    statusChoices = ( ('Tn','Tentative'), ('Sc','Scheduled'), ('Cu','Coming Up This Week'), ('Ed','Event Day'), ('Cl','Closed'), ('Pv','Payments Verified') )
    eventStatus = models.CharField('Event Status', max_length=20, choices=statusChoices, default='Sc')

    def __str__(self):
        return self.name

class Attendee(models.Model):    
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField('Name', null=True, max_length=120)
    contact = models.CharField('Contact Number', null=True, max_length=10)
    ageChoices = (('1', 'One'),('2', 'Two'),('3', 'Three'),('4', 'Four'),('5','Five'),('6', 'Six'),('7', 'Seven'),('8', 'Eight'),
        ('9', 'Nine'),('10', 'Ten'),('11', 'Eleven'),('12', 'Twelve'),('13', 'Thirteen'),('14', 'Fourteen'),('15', 'Fifteen'),('16', 'Sixteen'))
    ageOfParticipants = models.CharField('Age', max_length=20, choices=ageChoices, default='1')
    paymentStatus = models.BooleanField('Aprroved', default=False)
    approver = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name