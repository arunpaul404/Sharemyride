from django.conf.urls import url
from rating import views
urlpatterns=[
    url('req/',views.rating)
]
