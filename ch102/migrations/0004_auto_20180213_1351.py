# Generated by Django 2.0.2 on 2018-02-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ch102', '0003_auto_20180213_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='title',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='safety',
            name='title',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]