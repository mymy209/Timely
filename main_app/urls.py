from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dates/', views.date_list, name='dates_index'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('date/date_detail/<slug:date>/', views.date_details, name="date_details"),
    path('accounts/signup/', views.signup, name='signup'),
    path('event/event_detail/<int:pk>', views.EventDetail.as_view(), name="event_details"),
]
