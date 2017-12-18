from django.conf.urls import url, include

from . import views

app_name='golf'
urlpatterns = [
     url(r'^new/$', views.create, name="create"),
     url(r'^(?P<pk>\d+)/$', views.detail, name="detail"),
     url(r'$', views.list, name='list'),
]
