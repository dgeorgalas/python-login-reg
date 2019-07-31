from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows/new$', views.index), 
    url(r'^shows/(?P<show_id>\d+)$', views.show),
    url(r'^shows$', views.all_shows),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<show_id>\d+)/delete', views.delete),
    url(r'^shows/(?P<show_id>\d+)/update', views.update),
]