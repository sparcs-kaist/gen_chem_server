from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^notice/', views.notice, name='notice'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^evaluation/', views.evaluation, name='evaluation'),
    url(r'^safety/', views.safety, name='safety'),
    url(r'^links/', views.links, name='links'),
    url(r'^contact/', views.contact, name='contact'),
]