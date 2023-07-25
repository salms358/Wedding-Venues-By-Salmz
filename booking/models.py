from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0, "Booking Pending"), (1, "Booking Accepted"))


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)
    client_email = models.CharField(max_length=50)


def __str__(self):
    return str(self.user)


class Bookings(models.Model):
    venue = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    name = models.CharField(max_length=25)
    capacity = models.IntegerField


class Meta:
    ordering = ['-booking_date']