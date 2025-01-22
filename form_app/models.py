from django.db import models

# Create your models here.
from django.db import models

class RegForm(models.Model):
    Full_name = models.CharField(max_length=100)
    Date_of_birth = models.DateField()
    Gender = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.Full_name}, {self.Date_of_birth}, {self.Gender}, {self.mobile_number}, {self.email}, {self.address}"


