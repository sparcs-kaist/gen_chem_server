from django.db import models
from django.dispatch import receiver

import time
import os

# Create your models here.

basic_file_path = 'ch101/download'


def file_path (instance, filename):
    (year, name) = (instance.year, instance.name)

    path = basic_file_path
    path += '/' + str (year) + '/'

    type = filename.split ('.') [-1]
    path += (name + '.' + type)

    return path


class Notice(models.Model):
    title = models.TextField()
    description = models.TextField()
    event_date = models.DateTimeField()
    post_date = models.DateTimeField()


class Schedule(models.Model):
    type = models.CharField(
        max_length=15,
        choices=(
            ('exam', 'exam'),
            ('quiz', 'quiz'),
            ('recitation', 'recitation'),
            ('lecture', 'lecture'),
        )
    )
    event_date = models.DateTimeField()
    description = models.TextField()


class Evaluation(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.TextField()


class Safety(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.TextField()


class Download(models.Model):
    now = time.localtime()
    this_year = now.tm_year
    year_choices = []
    for i in range (1980, this_year + 1):
        year_choices.append ((i, str (i)))

    name = models.TextField (default = None)
    year = models.IntegerField (default = this_year, choices = year_choices)
    file = models.FileField (default = None, upload_to = file_path, blank = True)

    class Meta:
        unique_together = ('name', 'year')

    def __str__ (self):
        return '(' + str (self.year) + ') ' + str (self.name)


class Contact(models.Model):
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    picture = models.TextField()


@receiver(models.signals.post_delete, sender = Download)
def auto_delete_file_on_delete (sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile (instance.file.path):
            os.remove (instance.file.path)