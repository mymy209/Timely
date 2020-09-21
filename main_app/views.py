from django.shortcuts import render
from .models import Event
from django.views.generic import ListView, 
from django.views.generic.edit import CreateView


# Create your views here.
def home(request):
    return render(request, 'home.html')

class  DateList(ListView):
    model = Event

class EventCreate(CreateView):
    model = Event
    fields = ['event_name', 'date', 'time', 'event_details']