from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="poultry_home"),
    path('journal/', views.journal, name="poultry_journal"),
    path('analytics/', views.analytics, name="poultry_analytics"),
    path('about/', views.about, name="poultry_about"),
]
