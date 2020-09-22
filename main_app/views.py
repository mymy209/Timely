from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .models import Event
from django.views.generic import ListView 
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def date_list(request):
    events = Event.objects.all()
    dates = dict.fromkeys(list(map(lambda event: event.date, events)), [])
    for event in events:
        dates[event.date].append(event)
    return render(request, 'main_app/date_list.html', {
        'events': dates
    })

@login_required
def date_details(request, date):
    events = Event.objects.filter(date=date)
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

