from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="publicHome"),
    path('event/<event_id>', views.event_page, name="publicEventPage"),
    path('attendeeCsv/<event_id>', views.attendee_csv, name="eventAttendeeCsv"),
    path('login/', views.login_page, name="Login"),
    path('logout/', views.logout_page, name="Logout"),
    path('password/', views.user_password, name="changePassword"),
    path('register', views.user_register, name="userRegister"),
]