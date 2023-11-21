from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=50)
    email = models.EmailField()
    cnic = models.CharField(max_length=15)
    addressOne = models.CharField(max_length=150)
    addressTwo = models.CharField(max_length=150)
    contact = models.CharField(max_length=11)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    # primary key 