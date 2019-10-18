from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .timetable import intercitybus_crawling, citybus_crawling
# Create your views here.


class InterCityTimeTabelView(APIView):

    def get(self, request):
        intercity = intercitybus_crawling()
        return Response({
            "intercity": intercity,
        })


class CityTimeTableView(APIView):

    def get(self, request):
        city = citybus_crawling()
        return Response({
            "city": city,
        })