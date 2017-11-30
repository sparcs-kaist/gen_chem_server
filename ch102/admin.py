from django.contrib import admin
from django.db import models
from ch102.models import *

# Register your models here.

admin.site.register(Notice)
admin.site.register(Schedule)
admin.site.register(Evaluation)
admin.site.register(Safety)
admin.site.register(Links)
admin.site.register(Contact)
