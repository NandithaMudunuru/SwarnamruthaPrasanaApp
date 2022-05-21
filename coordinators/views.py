from django.shortcuts import render, redirect
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import *
from .forms import *


def notSuperUser(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='Login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and not u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


@login_required
@notSuperUser
def user_profile(request):
    user = request.user
    if request.method == "POST":
        form = CoordinatorProfileUpdate(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Update Successful.'))
            return redirect('userProfile')

    else:
        form = CoordinatorProfileUpdate(instance=user)
        return render(request, "public/profile.html", {
            'form': form,
        })


@login_required
@notSuperUser
def coordinator_eventsBase(request):
    user = request.user
    event_list = Event.objects.filter(Coordinator=user)
    return render(request, "coordinators/events.html", {
        "event_list": event_list,
        "currentEvent": False,
    })


@login_required
@notSuperUser
def coordinator_event(request, event_id):
    user = request.user
    event_list = Event.objects.filter(Coordinator=user)
    currentEvent = Event.objects.get(pk=event_id)
    allAttendees = Attendee.objects.filter(event=currentEvent)
    attendees = Attendee.objects.filter(event=currentEvent, approver=user)
    numOfAttendees = len(attendees)
    numOfAllAttendees = len(allAttendees)
    amountCollected = numOfAttendees*50
    return render(request, "coordinators/events.html", {
        "event_list": event_list,
        "currentEvent": currentEvent,
        "attendees": attendees,
        "allAttendees": allAttendees,
        "numOfAttendees": numOfAttendees,
        "numOfAllAttendees": numOfAllAttendees,
        "amountCollected": amountCollected,
    })


@login_required
@notSuperUser
@csrf_exempt
def coordinator_home(request):
    fetched = False
    submitted = False
    user = request.user
    if request.method == "POST" and request.POST.get('formType')=='approve' :
        uniqueCode = request.POST.get('UniqueCode', None)
        attendeeId = int(uniqueCode.split("/")[1])
        attendee = Attendee.objects.get(pk=attendeeId)
        attendee.paymentStatus = True
        attendee.approver = user
        attendee.save()
        fetched = True
        submitted = True
        return render(request, "coordinators/attendeeCode.html", {
            'fetched': fetched,
            'submitted': submitted, 
            })
    elif request.method == "POST" and request.POST.get('formType')=='fetch':
        uniqueCode = request.POST.get('UniqueCode')
        eventId = int(uniqueCode.split("/")[0])
        attendeeId = int(uniqueCode.split("/")[1])
        try:
            attendee = Attendee.objects.get(pk=attendeeId)
        except:
            messages.success(request, "Invalid code. Please try again.")
            return redirect('coordinatorHome')
        form = AttendeeApprovalForm(instance=attendee)
        if eventId == attendee.event.id:
            if Event.objects.get(pk=eventId).Coordinator == user:
                fetched = True
                return render(request, "coordinators/attendeeCode.html", {
                    'form': form,
                    'UniqueCode': uniqueCode,
                    'fetched': fetched,
                    'submitted': submitted, 
                })
            else:
                messages.success(request, "You are not authorised to approve this attendee. Contact the organisers to make you the coordinator for event named: {} and try again.".format(Event.objects.get(pk=eventId).name))
                return redirect('coordinatorHome')
        else:
            messages.success(request, "Invalid code. Please try again.")
            return redirect('coordinatorHome')
    else:
        return render(request, "coordinators/attendeeCode.html", {
            'fetched': fetched,
            'submitted': submitted, 
        })