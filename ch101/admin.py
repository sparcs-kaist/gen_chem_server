from django.contrib import admin
from django.db import models
from ch101.models import *
# Register your models here.

admin.site.register(Notice)
admin.site.register(Schedule)
admin.site.register(Download)
admin.site.register(Contact)
