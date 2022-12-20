from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class booking(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


def __STR__(self):
    return self.name
