from rest_framework import serializers
from .models import BusTimetableModel, BusCityModel


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