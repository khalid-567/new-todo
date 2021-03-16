from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Customer(models.Model):
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    email=models.EmailField()
    added_by = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.first_name

