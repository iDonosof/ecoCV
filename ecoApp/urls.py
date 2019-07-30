from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_information, name='event_information')
]
