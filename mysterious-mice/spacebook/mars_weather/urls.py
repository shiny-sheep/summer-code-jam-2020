from django.urls import path
from .views import CurrentWeatherView, WeekWeatherView

urlpatterns = [
    path("weather/current/", CurrentWeatherView.as_view(), name="current_weather"),
    path("weather/week/", WeekWeatherView.as_view(), name="week_weather"),
]
