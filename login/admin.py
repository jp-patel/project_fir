from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.civilianModel)
admin.site.register(models.officerModel)
