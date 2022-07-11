from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.jurisdictionModel)
admin.site.register(models.reportModel)