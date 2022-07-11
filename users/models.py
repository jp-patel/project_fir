from datetime import datetime
from django.db import models
from login.models import civilianModel, officerModel

# Create your models here.

class userHistoryModel(models.Model):
    title = models.CharField(max_length = 50, blank = True, default = '')
    civilian = models.ForeignKey(civilianModel, on_delete = models.CASCADE, blank = True, default = None, null = True)
    officer = models.ForeignKey(officerModel, on_delete = models.CASCADE, blank = True, default = None, null = True)
    datetime = models.DateTimeField(default = datetime.now)
    type = models.BooleanField(default = False)
    issue = models.PositiveSmallIntegerField(default = 0)
    seen = models.BooleanField(default = False)
    def __str__(self):
        return self.title

class userNotificationModel(models.Model):
    title = models.CharField(max_length = 50, blank = True, default = '')
    message = models.CharField(max_length = 150, blank = True, default = '')
    click = models.CharField(max_length = 20, blank = True, default = '')
    civilian = models.ForeignKey(civilianModel, on_delete = models.CASCADE, blank = True, default = None, null = True)
    officer = models.ForeignKey(officerModel, on_delete = models.CASCADE, blank = True, default = None, null = True)
    datetime = models.DateTimeField(default = datetime.now)
    seen = models.BooleanField(default = False)
    def __str__(self):
        return self.title
