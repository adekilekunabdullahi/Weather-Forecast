from django.urls import path

from WeatherApp import views

urlpatterns = [
    path("Weather", views.show_temp, name='show_here'),
    path("Weather/somewhere", views.somewhere, name='somewhere')
]