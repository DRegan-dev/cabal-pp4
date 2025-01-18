from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.http import HttpResponse

# Create your views here.
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        # Redirect based on user role
        if user.role == 'attendee':
            return redirect('attendee_dashboard')
        elif user.role == 'promoter':
            return redirect('venue_dashboard')
        elif user.role == 'Artist':
            return redirect('events_dashboard')
    else:
        messages.error(request, 'Invalid username or password.')

return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def venue_dashboard(request):
    return render(request, 'venue_dashboard.html')

def artist_dashboard(request):
    return render(request, 'artist_dashboard.html')

def attendee_dashboard(request):
    return render(request, 'attendee_dashboard.html')

def events_dashboard(request):
    return render(request, 'events_dashboard.html', {'events': events})

def create_event (request):
    return HttpResponse("This is the Create Event page")

def events_list(request):
    return render(request, 'events_list.html')

