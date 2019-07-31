from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^contribute$', views.contribute),
    url(r'^quotes$', views.quotes),
    url(r'^users/(?P<quote_user_id>\d+$)', views.users),
    url(r'^add_to_favorites/(?P<non_fav_id>\d+$)', views.add_to_favorites),
    url(r'^remove/(?P<favorite_id>\d+$)', views.remove),
    url(r'^logout', views.logout),
]