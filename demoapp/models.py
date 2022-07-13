
from django.db import models

class TaskDb(models.Model):
    EmployeeID=models.CharField(max_length=20)
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Location=models.CharField(max_length=20)
    Designation=models.CharField(max_length=20)
    Salary=models.IntegerField()
    PhoneNumber=models.CharField(max_length=20)
    EmailID=models.CharField(max_length=20)

    class Meta:
        db_table="employee_details"
