from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dates/', views.event_list, name='dates_index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
]
