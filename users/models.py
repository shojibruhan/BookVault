from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
    memebership_date= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username


class Author(models.Model):
    name= models.CharField(max_length=100)
    biography= models.TextField(blank=True, null= True)


    def __str__(self):
        return self.name
    