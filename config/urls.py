from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timetable/', include('timetable.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
