from django.urls import path
from . import views

urlpatterns = [
    path('venue-dashboard/', views.venue_dashboard, name='venue_dashboard'),
    path('attendee-dashboard/', views.attendee_dashboard, name='attendee_dashboard'),
]