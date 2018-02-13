from django.db import models

# Create your models here.

basic_file_path = 'ch102/download'

def file_path_1(instance, filename):
    title = instance.title

    path = basic_file_path
    path += '/' + title + '/' + str(1) + '/'
    path += filename

    return path

def file_path_2(instance, filename):
    title = instance.title

    path = basic_file_path
    path += '/' + title + '/' + str(2) + '/'
    path += filename

    return path

def file_path_3(instance, filename):
    title = instance.title

    path = basic_file_path
    path += '/' + title + '/' + str(3) + '/'
    path += filename

    return path

def file_path_4(instance, filename):
    title = instance.title

    path = basic_file_path
    path += '/' + title + '/' + str(4) + '/'
    path += filename

    return path

def file_path_5(instance, filename):
    title = instance.title

    path = basic_file_path
    path += '/' + title + '/' + str(5) + '/'
    path += filename

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
        null=True,
    )
    link = models.URLField(
        null=True,
    )
    file1 = models.FileField(
        upload_to=file_path_1,
        null=True,
    )
    file2 = models.FileField(
        upload_to=file_path_2,
        null=True,
    )
    file3 = models.FileField(
        upload_to=file_path_3,
        null=True,
    )
    file4 = models.FileField(
        upload_to=file_path_4,
        null=True,
    )
    file5 = models.FileField(
        upload_to=file_path_5,
        null=True,
    )


class Contact(models.Model):
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    picture = models.TextField()
