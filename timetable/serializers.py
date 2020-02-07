from rest_framework import serializers
from .models import BusTimetableModel, BusCityModel, InterCityModel, InterCityTimetableModel


class BusTimetableSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusTimetableModel
        fields = (
            'bus_time',
            'time',
        )


class BusCityListSerializer(serializers.ModelSerializer):
    class Meta:

        model = BusCityModel
        fields = (
            'id',
            'city',
        )


class BusCitySerializer(serializers.ModelSerializer):

    time_table = BusTimetableSerializer(read_only=True, many=True)

    class Meta:
        model = BusCityModel
        fields = (
            'city',
            'adult_fee',
            'teenager_fee',
            'child_fee',
            'time_table',
        )


class InterCityTimeTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterCityTimetableModel
        fields = (
            's_city',
            'time',
        )


class InterCitySerializer(serializers.ModelSerializer):

    intercity_table = InterCityTimeTableSerializer(read_only=True, many=True)

    class Meta:
        model = InterCityModel
        fields = (
            'city',
            'intercity_table',
        )

