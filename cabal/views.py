from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def venue_dashboard(request):
    return render(request, 'venue_dashboard.html')