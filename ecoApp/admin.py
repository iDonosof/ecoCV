from django.contrib import admin
from .models import Profile, Curriculum, Event, Company

# Register your models here.
admin.site.register(Profile)
admin.site.register(Curriculum)
admin.site.register(Event)
admin.site.register(Company)