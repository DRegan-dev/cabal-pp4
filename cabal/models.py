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
# Artist/Band model
class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    profile_description = models.TextField()
    past_events = models.Manager('Event', related_name='Historical_artists')

# Ratings between Artists and Venues
class VenueRating(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    rating = models.IntegerField() #Scale 1-5
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

# Events Model 
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASACADE, related_name='events')
    artists = models.ManyToManyField(Artist, related_name='events')
    attendees = models.ManyToManyField('Attendee', through='Ticket', related_name='events')
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)