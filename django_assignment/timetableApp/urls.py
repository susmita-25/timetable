from .views import timetable_view
from django.urls import path

urlpatterns = [
    path('timetable',timetable_view,name="timetable_view")
]
