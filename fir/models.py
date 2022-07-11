from datetime import datetime
from django.db import models

# Create your models here.

class jurisdictionModel(models.Model):
    division = models.CharField(max_length = 50)
    def __str__(self):
        return self.division

from login.models import civilianModel, officerModel

class reportModel(models.Model):
    division = models.ForeignKey(jurisdictionModel, on_delete = models.CASCADE, blank = True, default = None, null = True)
    subject = models.CharField(max_length = 30, blank = True, default = '')
    concern = models.TextField(blank = True, default = '')
    address = models.CharField(max_length = 30, blank = True, default = '')
    intersection = models.CharField(max_length = 30, blank = True, default = '')
    day = models.DateField(blank = True, default = None, null = True)
    time = models.TimeField(blank = True, default = None, null = True)
    frequency = models.PositiveSmallIntegerField(default = 0)
    complainee = models.CharField(max_length = 50, blank = True, default = '')
    complainee_address = models.TextField(blank = True, default = '')
    city = models.CharField(max_length = 20, blank = True, default = '')
    pincode = models.PositiveIntegerField(blank = True, default = 0)#max_length = 6
    phone = models.PositiveIntegerField(blank = True, default = 0)#max_length = 10
    civilian = models.ForeignKey(civilianModel, on_delete = models.CASCADE, blank = True, default = None, null = True)
    officer = models.ForeignKey(officerModel, on_delete = models.CASCADE, blank = True, default = None, null = True)
    date = models.DateTimeField(default = datetime.now)
    label = models.CharField(max_length = 10, default = 'muted')
    status = models.PositiveSmallIntegerField(default = 0)
    def __str__(self):
        return self.subject

'''
class draftModel(models.Model):
    division = models.ForeignKey(jurisdictionModel, on_delete = models.CASCADE, default = '')
    subject = models.CharField(max_length = 30, default = '')
    concern = models.TextField(default = '')
    address = models.CharField(max_length = 30, default = '')
    intersection = models.CharField(max_length = 30, default = '')
    day = models.DateField(default = 0)
    time = models.TimeField(default = 0)
    frequency = models.PositiveSmallIntegerField(default = 0)
    complainee = models.CharField(max_length = 50, default = '')
    complainee_address = models.TextField(default = '')
    city = models.CharField(max_length = 20, default = '')
    pincode = models.PositiveIntegerField(default = 0)#max_length = 6
    phone = models.PositiveIntegerField(default = 0)#max_length = 10
    email = models.ForeignKey(civilianModel, on_delete = models.CASCADE, default = '')
    date = models.DateTimeField(default = datetime.now)
    status = models.PositiveSmallIntegerField(default = 0)
    def __str__(self):
        return self.subject
'''