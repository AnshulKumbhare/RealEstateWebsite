from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class testimonial(models.Model):
    testimony = models.CharField(max_length = 300)
    tpname = models.CharField(max_length = 50)
    position = models.CharField(max_length = 30)
    companyname = models.CharField(max_length = 50)

class contact(models.Model):
    firstname = models.CharField(max_length = 50)
    middlename = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 80)
    mob1 = models.BigIntegerField(verbose_name = "Mobile 1")
    mob2 = models.BigIntegerField(verbose_name = "Mobile 2")
    address = models.CharField(max_length = 200)
    msg = models.CharField(max_length = 500)

class shelteragents(models.Model):
    agentname = models.CharField(max_length = 50)
    year = models.IntegerField()
    psold = models.IntegerField()
    agentimage = models.ImageField(upload_to='image')
    is_active = models.BooleanField(default = True, verbose_name = "Available")

class shelterproperties(models.Model):
    PTYPE1 = ((1, 'Land'), (2, 'Residential'), (3, 'Commercial'), (4, 'Industrial'))
    PTYPE2 = ((1, 'Sale'), (2, 'Rent'))
    firstname = models.CharField(max_length = 50)
    middlename = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    mob1 = models.BigIntegerField()
    mob2 = models.BigIntegerField()
    address = models.CharField(max_length = 500)
    city = models.CharField(max_length = 50)
    propertyname = models.CharField(max_length = 100)
    ptype1 = models.IntegerField(choices = PTYPE1)
    ptype2 = models.IntegerField(choices = PTYPE2)
    beds = models.IntegerField()
    area = models.IntegerField()
    price = models.BigIntegerField()
    description = models.CharField(max_length = 130)
    pimage = models.ImageField(upload_to= 'image')

class bookedproperty(models.Model):
    bookingid = models.CharField(max_length = 50)
    uid = models.ForeignKey(User, on_delete = models.CASCADE, db_column = "uid")
    pid = models.ForeignKey(shelterproperties, on_delete = models.CASCADE, db_column = "pid")