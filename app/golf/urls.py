from django.conf.urls import url, include

from . import views

app_name='golf'
urlpatterns = [
    url(r'^teams/', include('golf.teams.urls', namespace='teams')),
    url(r'^player/', include('golf.player.urls', namespace='player')),
    url(r'^$', views.index, name='home'),
]
