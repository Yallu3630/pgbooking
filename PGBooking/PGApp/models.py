from django.db import models

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=30)
    phno = models.CharField(max_length=13)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=13)

class room(models.Model):
    room_name = models.CharField(max_length=13)
    room_no = models.CharField(max_length=13)
    cap = models.CharField(max_length=20)
    rent_room = models.CharField(max_length=13)
    description = models.CharField(max_length=130)

class bookingrooms(models.Model):
    booked_user = models.CharField(max_length=30)
    booked_room_name = models.CharField(max_length=13)
    booked_room_no = models.CharField(max_length=13)
    booked_cap = models.CharField(max_length=20)
    booked_rent_room = models.CharField(max_length=13)
    booked_description = models.CharField(max_length=130)
    booked_date =models.CharField