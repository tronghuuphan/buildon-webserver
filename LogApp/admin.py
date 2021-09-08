from django.contrib import admin
from LogApp.models import Person, Camera, Tracking
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    ordering = ['location']

@admin.register(Tracking)
class TrackingAdmin(admin.ModelAdmin):
    list_display = ['idPeople', 'idCam', 'idContact', 'time']
    ordering = ['idPeople']