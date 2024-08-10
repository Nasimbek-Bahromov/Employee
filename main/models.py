from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

ADMIN, STAFF = ('admin', 'staff')
MALE, FEMALE = ('male', 'female')


class Employee(AbstractUser):
    ROLE = (
        (ADMIN, ADMIN),
        (STAFF, STAFF)
    )
    GENDER = (
        (MALE, MALE),
        (FEMALE, FEMALE)
    )
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices = GENDER)
    position = models.CharField(max_length=255, null=True, blank=True)
    workplace = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    salary = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(default=datetime.datetime.now)
    is_staff = models.CharField(max_length=10, choices=ROLE)

    def __str__(self):
        return self.first_name

    

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return self.employee.first_name
