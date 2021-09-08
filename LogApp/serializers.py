from django.db.models import fields
from rest_framework import serializers
from LogApp.models import Person, Camera, Tracking

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'
    
class TrackingSerializer(serializers.ModelSerializer):
    idPeople = PersonSerializer()
    idContact = PersonSerializer()
    class Meta:
        model = Tracking
        fields = ('id', 'idPeople', 'idCam', 'idContact', 'date', 'time')