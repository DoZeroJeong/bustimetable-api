from django.contrib import admin
from .models import BusTimetableModel, BusCityModel
# Register your models here.


class TimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'bus_time', 'time']


admin.site.register(BusTimetableModel, TimeAdmin)
admin.site.register(BusCityModel)