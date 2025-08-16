from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=15,blank=True)
    subject=models.CharField(max_length=100,blank=True)
    qualification=models.CharField(max_length=200,blank=True)
    experience_years=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.get_full_name()}-{self.subject}"