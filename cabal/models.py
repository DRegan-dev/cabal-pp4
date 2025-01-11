from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#Custom User Model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('promoter', 'Promoter/Venue'),
        ('artist', 'Band/Artist'),
        ('attendee', 'Attendee'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

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
    past_events = models.ManyToManyField('Event', related_name='historical_events')

# Ratings between Artists and Venues
class VenueRating(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    rating = models.IntegerField() #Scale 1-5
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Validate rating is between 1 and 5
        if not (1 <= self.rating <= 5):
            raise ValidationError("Rating must be between 1 and 5.")

# Events Model 
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    artists = models.ManyToManyField(Artist, related_name='events')
    attendees = models.ManyToManyField('Attendee', through='Ticket', related_name='events')
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class EventStatistics(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='statistics')
    tickets_sold = models.IntegerField(default=0)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)

class Attendee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events_registered = models.ManyToManyField(Event, through='Ticket', related_name='registered_attendees')

class Ticket(models.Model):
    attendee = models.ForeignKey('Attendee', on_delete=models.CASCADE, related_name='tickets')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='tickets')
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.event.title} - {self.attendee.user.username}"

