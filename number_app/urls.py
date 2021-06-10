from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),	
    path('counting_guess', views.counting_guess),
    path('low', views.low),
    path('high', views.high),
    path('correct', views.correct)
]