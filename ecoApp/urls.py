from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_information, name='event_information'),
    path('login/', views.login, name='login'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('profile/', views.profile, name='profile'),
    path('signin/', views.signin, name='signin')
]
