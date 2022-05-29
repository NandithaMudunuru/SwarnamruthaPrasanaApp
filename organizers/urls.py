from django.urls import path
from . import views

urlpatterns = [
    path('coordinator_redirect', views.coordinator_redirect, name="coordinatorRedirect"),
    path('profile', views.organizer_profile, name="organizerProfile"),
    path('events', views.organizer_eventsBase, name="organizerEventsBase"),
    path('events/<event_id>', views.organizer_event, name="organizerEvent"),
    path('newEvent', views.new_event, name="newEvent"),
    path('venues', views.venues_Base, name="organizerVenues"),
    path('venue', views.venue_Form, name="newVenue"),
    path('venue/<venue_id>', views.venue_Form, name="updateVenue"),
    path('deleteVenue/<venue_id>', views.venues_Delete, name="deleteVenue"),
]