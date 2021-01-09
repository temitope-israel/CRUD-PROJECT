from django.db import models
from django import forms

# Create your models here.
class Registration(models.Model):
    child_name = models.CharField(max_length=70)
    child_age = models.IntegerField(default=0)
    child_dob = models.DateField()
    MALE = "MALE"
    FEMALE = "FEMALE"
    SELECT = "SELECT"
    CHILD_GENDER_CHOICES = [
        (SELECT, 'Select'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    child_gender = models.CharField(max_length=6, null=False, choices=CHILD_GENDER_CHOICES, default=SELECT)
    mother_name = models.CharField(max_length=70, verbose_name="mother name")
    mother_age = models.IntegerField(default=0)

class User(models.Model):
    username = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)