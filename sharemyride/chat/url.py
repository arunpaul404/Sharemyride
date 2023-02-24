from django.conf.urls import url
from chat import views
urlpatterns=[
    url('req/',views.chat)
]