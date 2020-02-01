from django.urls import path
from .views import *


urlpatterns = [
    path('inje/<int:pk>', BusTimeTableListView.as_view()),
    path('inje/', BusCityListView.as_view()),
]