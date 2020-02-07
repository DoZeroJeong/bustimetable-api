from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BusCityModel, InterCityModel
from .serializers import BusCitySerializer, BusCityListSerializer, InterCitySerializer
from django.http import Http404
# Create your views here.


class BusTimeTableListView(APIView):

    def get_object(self, pk):
        try:
            return BusCityModel.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk):
        city = self.get_object(pk)
        serializer = BusCitySerializer(city)
        return Response(serializer.data)


class BusCityListView(APIView):

    def get(self, request):
        city = BusCityModel.objects.all().order_by('id')
        serializer = BusCityListSerializer(city, many=True)
        return Response(serializer.data)


class InterCityView(APIView):

    def get_object(self, pk):
        try:
            return InterCityModel.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk):
        intercity = self.get_object(pk)
        serializer = InterCitySerializer(intercity)
        return Response(serializer.data)
