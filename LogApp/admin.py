from django.contrib import admin
from LogApp.models import Person, Camera, Tracking, PersonLog
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
    list_display = ['idPeople', 'idCam', 'idContact','date', 'time']
    ordering = ['idPeople']

@admin.register(PersonLog)
class PersonLogAdmin(admin.ModelAdmin):
    list_display = ['idPeople', 'mask', 'idCam', 'date', 'time']
    ordering = ['idPeople']
