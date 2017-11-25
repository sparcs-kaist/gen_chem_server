from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^notice/', views.notice, name='notice'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^download/', views.download, name='download'),
    url(r'^contact/', views.contact, name='contact'),
]