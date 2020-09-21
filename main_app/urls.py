from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dates/', views.DateList.as_view(), name='date_index')
]
