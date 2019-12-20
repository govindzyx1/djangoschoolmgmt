from django.urls import path
from . import views

urlpatterns =[
    path(r'form',views.StudForm,name='StudForm'),
    path(r'home',views.home,name='home'),
    path(r'records',views.mydb,name='mydb'),
    ]
