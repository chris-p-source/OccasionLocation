from django.contrib import admin

# Register your models here.
from .models import Event, EventAttendance

admin.site.register(Event)
admin.site.register(EventAttendance)
