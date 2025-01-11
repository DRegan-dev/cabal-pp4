from django.urls import path
from . import views

urlpatterns = [
    path('venue-dashboard/', views.venue_dashboard, name='venue_dashboard'),
]