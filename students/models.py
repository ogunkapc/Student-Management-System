from django.db import models

# Create your models here.


class Student(models.Model):
    matric_number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    department = models.CharField(max_length=50)
    program_of_study = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
