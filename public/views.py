from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.http import HttpResponse
from django.contrib import messages
from django.core.cache import cache
from .models import *
from .forms import *
import csv

# Create your views here.
def home(request):
    event_list = Event.objects.all().order_by('start_time')
    return render(request, "public/eventListPage.html", {
        'event_list': event_list,
    })

def event_page(request, event_id):
    event = Event.objects.get(pk=event_id)
    venue = Venue.objects.get(pk=event.venue.id)
    event_list = venue.event_set.all().order_by('start_time')
    submitted = False
    if request.method == "POST":
        form = AttendeeRegistrationForm(request.POST)
        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.event = event
            attendee.save()
            messages.success(request,"{event}/{attendee}".format(event=event_id,attendee=attendee.id) )
            return 	HttpResponseRedirect('event\{}?submitted=True'.format(event_id))

    else:
        form = AttendeeRegistrationForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, "public/eventPage.html", {
        'event_list': event_list,
        'event': event,
        'form':form,
        'submitted':submitted,
    })


@csrf_exempt
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('Username', None)
        password = request.POST.get('Password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Redirect to a success page.
            login(request, user)
            next_url = cache.get('next')
            if next_url:
                cache.delete('next')
                return HttpResponseRedirect(next_url)
            else:
                return redirect('coordinatorHome')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Invalid username or password. Please try again.")
            return redirect('Login')
    else:
        cache.set('next', request.GET.get('next', None))
        if request.user.is_authenticated:
            next_url = cache.get('next')
            if next_url:
                cache.delete('next')
                return HttpResponseRedirect(next_url)
            else:
                return redirect('coordinatorHome')
        else:
            return render(request, "public/login.html", {})


def logout_page(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('Login')


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Successful.'))
            return redirect('userProfile')
    else:
        form = UserCreationForm()
        return render(request, "public/register.html", {
            'form': form,
        })


@login_required
def user_password(request):
    user = request.user
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Update Successful.'))
            login(request, user)
            return redirect('userProfile')

    else:
        form = PasswordChangeForm(user=user)
        return render(request, "public/passwordChange.html", {
            'form': form,
        })


@login_required
def attendee_csv(request, event_id):
    event = Event.objects.get(pk=event_id)
    print(event.name)
    attendees = Attendee.objects.filter(event=event)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=attendees_{}.csv'.format(event.venue.name+'_'+event.start_time.strftime('%B'))
    writer = csv.writer(response)
    writer.writerow(['Name', 'Age', 'Phone', 'Payment Status', 'Approver'])
    for attendee in attendees:
        writer.writerow([attendee.name, attendee.ageOfParticipants, attendee.contact, attendee.paymentStatus, attendee.approver])
    return response