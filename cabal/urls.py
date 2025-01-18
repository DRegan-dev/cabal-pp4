from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('venue-dashboard/', views.venue_dashboard, name='venue_dashboard'),
    path('attendee-dashboard/', views.attendee_dashboard, name='attendee_dashboard'),
    path('events-dashboard/', views.events_dashboard, name='events_dashboard'),
    path('create-event/', views.create_event, name='create_event'),
    path('events/', views.events_list, name='events_list'),
    path('artist-dashboard/', views.artist_dashboard, name='artist_dashboard'),
]