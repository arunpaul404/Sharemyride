from django.conf.urls import url
from complaint import views
urlpatterns=[
    url('view/',views.complaint),
    url('post/',views.postcmpt),
    url('postrply/',views.postrply),
    url('viewrply/',views.viewrply),
]