from django.shortcuts import render

# Create your views here.

from django.conf.urls import url
from vehicles import views
urlpatterns=[
    url('rehveh/',views.regvehicle),
    url('mngveh/',views.mngveh),
]
