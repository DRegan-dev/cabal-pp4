from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def venue_dashboard(request):
    return render(request, 'venue_dashboard.html')

def attendee_dashboard(request):
    return render(request, 'attendee_dashboard.html')

def events_dashboard(request):
    return render(request, 'events_dashboard.html', {'events': events})

def create_event (request):
    return HttpResponse("This is the Create Event page")

def events_list(request):
    return render(request, 'events_list.html')

