from django.conf.urls import url
from emergencyno import views
urlpatterns=[
    url('req/',views.emgno),
    url('view/',views.viewemg),
    url('alert/',views.alert),
]