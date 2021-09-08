from re import split
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from LogApp.models import Person, Camera, Tracking, PersonLog
from LogApp.serializers import PersonSerializer, CameraSerializer, TrackingSerializer, PersonLogSerializer 

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

import datetime
# Create your views here.
class PersonAPIView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PersonLogAPIView(APIView):
    def get_object(self, id):
        try:
            return PersonLog.objects.filter(idPeople=id)
        except PersonLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id_people_log):
        person = self.get_object(id_people_log)
        serializer = PersonLogSerializer(person, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TrackingAPIView(APIView):
    def get(self, request):
        tracking = Tracking.objects.all()
        serializer = TrackingSerializer(tracking, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TrackingByID(APIView):
    def get_object(self, id):
        try:
            return Tracking.objects.filter(idPeople=id)
        except Tracking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id_people):
        tracking = self.get_object(id_people)
        serializer = TrackingSerializer(tracking, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FindByDate(APIView):
    def get(self, request, selected_day):
        [year, month, day] = list(map(int, selected_day.split('-')))
        result = Tracking.objects.filter(date__startswith=datetime.date(year, month, day))
        serializer = TrackingSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

