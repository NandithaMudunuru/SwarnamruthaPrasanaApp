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
def organizer_eventsBase(request):
    user = request.user
    event_list = Event.objects.filter(Coordinator=user)
    return render(request, "organizers/events.html", {
        "event_list": event_list,
        "currentEvent": False,
    })


@login_required
@SuperUser
def organizer_event(request, event_id):
    user = request.user
    event_list = Event.objects.filter(Coordinator=user)
    currentEvent = Event.objects.get(pk=event_id)
    allAttendees = Attendee.objects.filter(event=currentEvent)
    attendees = Attendee.objects.filter(event=currentEvent, approver=user)
    numOfAttendees = len(attendees)
    numOfAllAttendees = len(allAttendees)
    amountCollected = numOfAttendees*50
    return render(request, "organizers/events.html", {
        "event_list": event_list,
        "currentEvent": currentEvent,
        "attendees": attendees,
        "allAttendees": allAttendees,
        "numOfAttendees": numOfAttendees,
        "numOfAllAttendees": numOfAllAttendees,
        "amountCollected": amountCollected,
    })


@login_required
@SuperUser
@csrf_exempt
def organizer_home(request):
    return render(request, "organizers/home.html", {
    })
