from django.db import models

# Create your models here.


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

    def __str__(self):
        return str(self.event_date)


class Evaluation(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.TextField()

    def __str__(self):
        return self.title


class Safety(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.TextField()

    def __str__(self):
        return self.title


class Links(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=50,
    )
    description = models.TextField(
        null=False,
        blank=True,
    )
    link = models.URLField()


class Contact(models.Model):
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    picture = models.TextField()
