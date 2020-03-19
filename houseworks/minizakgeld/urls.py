from django.urls import path, include
from .import views

urlpatterns = [
    path ('', views.index, name="index"),
    path('minizakgeld_details', views.minizakgeld_details, name="minizakgeld_details"),
    path('minizakgeld_add', views.minizakgeld_add, name="minizakgeld_add"),
    path('person_1', views.person_1, name="person_1"),
]

