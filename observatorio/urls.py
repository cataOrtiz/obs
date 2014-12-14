from django.conf.urls import patterns, url

from observatorio import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
