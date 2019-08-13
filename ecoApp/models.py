from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rut = models.IntegerField(default = -1)
    dv = models.CharField(max_length = 1, default = -1)
    birth_date = models.DateField(auto_now = False, auto_now_add = False, null = True)
    address = models.CharField(max_length = 500, null = True, blank = True)
    phone_number = models.BigIntegerField(null = True, blank = True)
    available = models.BooleanField(default = True)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created: 
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Curriculum(models.Model):
    user_profile = models.ForeignKey('Profile', on_delete = models.CASCADE)
    academic_training = models.TextField(null = True, blank = True)
    further_training = models.TextField(null = True, blank = True)
    work_experience = models.TextField(null = True, blank = True)
    languages = models.TextField(null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    knowledge = models.TextField(null = True, blank = True)

class Company(models.Model):
    name = models.CharField(max_length = 255, default = 'Sin nombre')
    username = models.CharField(max_length = 255, null = False, blank = False)
    password = models.CharField(max_length = 255, null = False, blank = False)
    description = models.CharField(max_length = 500, null = True, blank = True)

class Event(models.Model):
    name = models.CharField(max_length = 255, default = 'Sin nombre')
    event_date = models.DateField(auto_now = False, auto_now_add = False, null = True)
    time_start = models.TimeField(auto_now = False, auto_now_add = False, null = True)
    time_finish = models.TimeField(auto_now = False, auto_now_add = False, null = True)
    description = models.CharField(max_length = 500, null = True, blank = True)
    event_map = models.FileField(upload_to = 'media', blank = True, null = True)

#Create one to many between Company and event 