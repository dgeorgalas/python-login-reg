from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^bears$', views.bears),
    url(r'^abe$', views.abe),
]