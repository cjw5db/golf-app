from django.conf.urls import url, include

from . import views

app_name='golf'
urlpatterns = [
     url(r'^new/$', views.create, name="create"),
     url(r'^(?P<pk>\d+)/generate/$', views.generate, name="generate"),
     url(r'^(?P<pk>\d+)/detail/$', views.detail, name="detail"),
     url(r'^(?P<pk>\d+)/delete/$', views.delete, name="delete"),
     url(r'^$', views.list, name='list'),
]
