from django.urls import path

from bus import views


urlpatterns = [
    path('<str:city>/', views.TimeTableView.as_view()),
]
