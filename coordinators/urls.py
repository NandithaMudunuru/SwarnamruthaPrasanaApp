from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.coordinator_home, name="coordinatorHome"),
    path('organizer_redirect', views.organizer_redirect, name="organizerRedirect"),
    path('profile', views.user_profile, name="userProfile"),
    path('events', views.coordinator_eventsBase, name="coordinatorEventsBase"),
    path('events/<event_id>', views.coordinator_event, name="coordinatorEvent"),
]