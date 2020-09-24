from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dates/', views.date_list, name='dates_index'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('date/date_detail/<slug:date>/', views.date_details, name="date_details"),
    path('accounts/signup/', views.signup, name='signup'),
    path('event/event_detail/<int:pk>', views.EventDetail.as_view(), name="event_details"),
    path('event/event_detail/<int:event_id>/delete/', views.event_delete, name="event_delete"),
    path('event/event_detail/<int:pk>/update/', views.EventUpdate.as_view(), name="event_update"),
    path('passed_dates/', views.passed_date_list, name="passed_dates_index"),
    path('search/', views.search_index, name="search_index"),
    path('search/results/', views.search_list, name="search_list"),
]
