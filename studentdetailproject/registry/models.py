from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    second_name=models.CharField(max_length=50)
    roll_no=models.IntegerField()
    standard = models.IntegerField()

    def __str__(self):
        return self.first_name + ' '+self.last_name