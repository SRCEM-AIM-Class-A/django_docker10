from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
path('',views.index, name='home'),
path("about/", views.about, name="about"),
# path("contact/", views.contact, name="contact"),
path("services/",views.services,name="services"),
path("home/",views.home,name="home"),
path("index/",views.index,name="index")
]