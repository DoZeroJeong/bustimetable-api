from django.contrib import admin
from .models import BusTimetableModel, BusCityModel, InterCityModel, InterCityTimetableModel
# Register your models here.


class TimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'bus_time', 'time']


class InterTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'city_id', 's_city', 'time']


class InterCityAdmin(admin.ModelAdmin):
    list_display = ['id', 'city']


admin.site.register(BusTimetableModel, TimeAdmin)
admin.site.register(BusCityModel)
admin.site.register(InterCityModel, InterCityAdmin)
admin.site.register(InterCityTimetableModel, InterTimeAdmin)