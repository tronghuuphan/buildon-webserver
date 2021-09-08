from django.urls import path, re_path
from LogApp.views import FindByDate, PersonAPIView, TrackingAPIView, TrackingByID, PersonLogAPIView

urlpatterns = [
    path('person/', PersonAPIView.as_view()),
    path('tracking/', TrackingAPIView.as_view()),
    path('tracking/<int:id_people>/', TrackingByID.as_view()),
    #path('search/date/<int:date>/', FindByDate.as_view()),
    re_path(r'^find/(?P<selected_day>\d{4}-\d{2}-\d{2})/$', FindByDate.as_view()),
    path('log/<int:id_people_log>/', PersonLogAPIView.as_view())
]
