from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#User roles for Promoters/Venues, Band/Artists, and Attendees
class User(models.Model):
    ROLE_CHOICES = [
        ('promoter', 'Promoter/Venue'),
        ('artist', 'Band/Artist'),
        ('attendee', 'Attendee'),
    ]
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

# Venue/Promoter Model
class Venue(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    ratings = models.ManyToManyField('Artist', through='VenueRating', related_name='rated_venues')