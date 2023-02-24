from django.shortcuts import render

# Create your views here.

from django.conf.urls import url
from booking import views
urlpatterns=[
    url('addbooking/',views.addbooking),
    url('bookingrqst/.',views.bookingrqst),
    url('bookingstatus/',views.bookingstatus),
    url('bookusr/',views.bookusr),
]