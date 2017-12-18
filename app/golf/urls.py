from django.conf.urls import url, include

from . import views

app_name='golf'
urlpatterns = [
    url(r'^$', views.index, name='home'),
]
