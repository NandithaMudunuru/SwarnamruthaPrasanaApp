from django.shortcuts import render, redirect
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import *
from .forms import *


def SuperUser(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='coordinatorRedirect'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def coordinator_redirect(request):
    return render(request, "organizers/coordinatorRedirect.html", {
    })


@login_required
@SuperUser
def organizer_profile(request):
    user = request.user
    if request.method == "POST":
        form = OrganizerProfileUpdate(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Update Successful.'))
            return redirect('organizerProfile')

    else:
        form = OrganizerProfileUpdate(instance=user)
        return render(request, "organizers/profile.html", {
            'form': form,
        })

@login_required
@SuperUser
def new_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            newEvent = form.save()
            event_id = newEvent.pk
            messages.success(request, ('New Event Successfully Created.'))
            return redirect('organizerEvent', event_id)

    else:
        form = EventForm()
        return render(request, "organizers/newEvent.html", {
            'form': form,
        })


@login_required
@SuperUser
def organizer_eventsBase(request):
    event_list = Event.objects.all()
    return render(request, "organizers/events.html", {
        "event_list": event_list,
        "currentEvent": False,
    })


@login_required
@SuperUser
def organizer_event(request, event_id):
    if request.method == "POST" and  request.POST.get('formType')=='Update Event':
        form = EventForm(request.POST, instance=Event.objects.get(pk=event_id))
        if form.is_valid():
            form.save()
            messages.success(request, ('Event update Successful.'))
            return redirect('organizerEvent', event_id)
    elif request.method == "POST" and  request.POST.get('formType')=='Delete Event':
        currentEvent = Event.objects.get(pk=event_id)
        currentEvent.delete()
        return redirect('organizerEventsBase')

    else:
        event_list = Event.objects.all()
        currentEvent = Event.objects.get(pk=event_id)
        allAttendees = Attendee.objects.filter(event=currentEvent)
        numOfAllAttendees = len(allAttendees)
        numOfApprovedAttendees = len(allAttendees.filter(paymentStatus=True))
        amountCollected = numOfApprovedAttendees*50
        totalAmount = numOfAllAttendees*50
        form = EventForm(instance=currentEvent)
        return render(request, "organizers/events.html", {
            "event_list": event_list,
            "currentEvent": currentEvent,
            "allAttendees": allAttendees,
            "numOfAllAttendees": numOfAllAttendees,
            "totalAmount": totalAmount,
            "amountCollected": amountCollected,
            "numOfApprovedAttendees": numOfApprovedAttendees,
            "form": form,
        })


@login_required
@SuperUser
def venues_Base(request):
    venues = Venue.objects.all()
    return render(request, "organizers/venues.html", {
        'venues':venues,
    })

@login_required
@SuperUser
def venues_Delete(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('organizerVenues')

@login_required
@SuperUser
def venue_Form(request, venue_id=False):
    if venue_id:
        venue = Venue.objects.get(pk=venue_id)
        if request.method == "POST":
            form = VenueForm(request.POST, instance=venue)
            if form.is_valid():
                form.save()
                messages.success(request, ('Venue Successfully Updated.'))
                return redirect('organizerVenues')

        else:
            form = VenueForm(instance=venue)
            return render(request, "organizers/newVenue.html", {
                'form': form,
            })
    else:
        if request.method == "POST":
            form = VenueForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ('New Venue Successfully Created.'))
                return redirect('organizerVenues')

        else:
            form = VenueForm()
            return render(request, "organizers/newVenue.html", {
                'form': form,
            })