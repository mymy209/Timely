from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .models import Event
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

@login_required
def date_list(request):
    events = Event.objects.filter(user=request.user)
    dates = dict.fromkeys(list(map(lambda event: event.date, events)), [])
    for event in events:
        dates[event.date].append(event)
    return render(request, 'main_app/date_list.html', {
        'events': dates
    })

@login_required
def date_details(request, date):
    events = Event.objects.filter(date=date, user=request.user)
    date_events = []
    for event in events:
        date_events.append(event)
    print('LOOK HERE PLEASE')
    print(date_events)
    return render(request, 'main_app/date_details.html', {
        'date_events': date_events
    })

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['event_name', 'date', 'time', 'event_details']
    
    def get_success_url(self):
        return reverse('dates_index')

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dates_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class EventDetail(LoginRequiredMixin, DetailView):
    model = Event

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['event_name', 'date', 'time', 'event_details']

def event_delete(request, event_id):
    event = Event.objects.get(id=event_id)
    Event.objects.filter(id=event_id).delete()
    return redirect('date_details', date = event.date)

def passed_date_list(request):
    events = Event.objects.filter(user=request.user)
    dates = dict.fromkeys(list(map(lambda event: event.date, events)), [])
    for event in events:
        dates[event.date].append(event)
    return render(request, 'main_app/passed_date_list.html', {
        'events': dates
    })

def search_index(request):
    return render(request, 'main_app/search_index.html')

def search_list(request):
    search = request.POST.get('search')
    events = Event.objects.filter(user=request.user, event_name__icontains=search)
    return render(request, 'main_app/search_list.html', {
        'events': events
    })