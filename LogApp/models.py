from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    
    def __str__(self) -> str:
        return str(self.id)

class Camera(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

class Tracking(models.Model):
    idPeople = models.ForeignKey('Person', related_name='id_people', on_delete=models.CASCADE)
    idCam = models.ForeignKey('Camera', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    idContact = models.ForeignKey('Person', related_name='id_contact', on_delete=models.CASCADE)