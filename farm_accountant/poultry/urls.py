from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="poultry_home"),
    path('about/', views.about, name="poultry_about"),
]
