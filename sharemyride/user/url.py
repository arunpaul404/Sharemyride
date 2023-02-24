from django.conf.urls import url
from user import views
urlpatterns=[
    url('avlusr/',views.avlusr),
    url('mngusr/',views.mnguser),
    url('regusr/',views.regusr)
]