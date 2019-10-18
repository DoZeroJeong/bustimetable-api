from django.urls import path
from .views import *


urlpatterns = [
    path('countryside', InterCityTimeTabelView.as_view()),
    path('downtown', CityTimeTableView.as_view()),
]