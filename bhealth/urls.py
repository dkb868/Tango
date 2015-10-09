from django.conf.urls import patterns, url
from bhealth import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'))