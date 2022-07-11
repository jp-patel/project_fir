from django.db import models

# Create your models here.
class civilianModel(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 15)
    # report = models.ForeignKey(reportModel, on_delete = models.CASCADE)#
    first_name = models.CharField(max_length = 20, default = '')
    last_name = models.CharField(max_length = 12, default = '')
    aadhar = models.PositiveIntegerField(default = 0)
    address = models.TextField(default = '')#
    city = models.CharField(max_length = 40, default = '')#
    pincode = models.PositiveIntegerField(default = 0)#
    phone = models.PositiveIntegerField(default = 0)#max_length = 10
    def __str__(self):
        return self.email

from fir.models import jurisdictionModel

class officerModel(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 15)
    division = models.ForeignKey(jurisdictionModel, on_delete = models.CASCADE)
    # report = models.ForeignKey(reportModel, on_delete = models.CASCADE)
    def __str__(self):
        return self.email
