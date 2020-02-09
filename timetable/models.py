from django.db import models

# Create your models here.


class BusCityModel(models.Model):
    city = models.CharField(max_length=100)
    adult_fee = models.CharField(max_length=100)
    teenager_fee = models.CharField(max_length=100)
    child_fee = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class BusTimetableModel(models.Model):
    city = models.ForeignKey(BusCityModel, on_delete=models.CASCADE, related_name='time_table')
    bus_time = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.bus_time