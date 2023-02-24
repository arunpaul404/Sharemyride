from django.conf.urls import url
from payment import views
urlpatterns=[
    url('req/',views.payment)
]