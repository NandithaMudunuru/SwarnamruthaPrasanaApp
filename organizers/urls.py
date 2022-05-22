from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.organizer_home, name="organizerHome"),
    path('coordinator_redirect', views.coordinator_redirect, name="coordinatorRedirect"),
    path('profile', views.organizer_profile, name="organizerProfile"),
    path('events', views.organizer_eventsBase, name="organizerEventsBase"),
    path('events/<event_id>', views.organizer_event, name="organizerEvent"),
]