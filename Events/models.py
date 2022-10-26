from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=35)
    image = models.ImageField(upload_to='images/')
    organiser = models.OneToOneField(User, on_delete=models.CASCADE)
    numberOfSeats = models.IntegerField()
    # numberOfBookedSeats =
    dateOfEvent = models.DateField()

    # def __str__(self):
    #     return self.name


# class Organiser(models.Model):
#     client = models.OneToOneField(
#         Client,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )

#     company = models.CharField(max_length=35)

#     def __str__(self):
#         return self.client
