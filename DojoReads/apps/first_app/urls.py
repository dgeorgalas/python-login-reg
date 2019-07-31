from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^books$', views.books),
    url(r'^books/add$', views.add_book),
]