from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.TextField()
    description = models.TextField()
    event_date = models.DateTimeField()
    post_date = models.DateTimeField()


class Schedule(models.Model):
    title = models.TextField()
    description = models.TextField()
    event_date = models.DateTimeField()
    type = models.TextField()
    class_name = models.TextField()


class Download(models.Model):
    name = models.TextField()
    date = models.DateTimeField()
    link = models.TextField()
    type = models.TextField()


class Contact(models.Model):
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    picture = models.TextField()
