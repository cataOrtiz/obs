from django.conf.urls import patterns, url

from observatorio import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^consultas/$', views.consultas, name='consultas'),
    url(r'^consultas/$','observatorio.views.consulta'),
    url(r'^respuestas/(\w*)$','observatorio.views.respuestas'),
)
