from .views import registration_view
from django.urls import path

urlpatterns = [
    path('',registration_view,name="registration-view")
]