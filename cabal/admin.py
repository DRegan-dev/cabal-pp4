from django.contrib import admin
from .models import User, Venue, Artist, VenueRating, Event, EventStatistics, Attendee, Ticket

# Register your models here.
admin.site.register(User)
admin.site.register(Venue)
admin.site.register(Artist)
admin.site.register(VenueRating)
admin.site.register(Event)
admin.site.register(EventStatistics)
admin.site.register(Attendee)
admin.site.register(Ticket)