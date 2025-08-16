from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    GENDER_CHOICES=[
        ('M','Male'),('F','Female')
    ]
    CLASS_CHOICES=[
        ('1', 'Class 1'),
        ('2', 'Class 2'),
        ('3', 'Class 3'),
        ('4', 'Class 4'),
        ('5', 'Class 5'),
        ('6', 'Class 6'),
        ('7', 'Class 7'),
        ('8', 'Class 8'),
        ('9', 'Class 9'),
        ('10', 'Class 10'),
        ('11', 'Class 11'),
        ('12', 'Class 12'),
    ]

    teacher=models.ForeignKey(User,on_delete=models.CASCADE,related_name='students')
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(blank=True)
    phone=models.CharField(max_length=15,blank=True)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    address=models.TextField(blank=True)
    class_level=models.CharField(max_length=2,choices=CLASS_CHOICES)
    parent_name=models.CharField(max_length=100)
    parent_email=models.EmailField(blank=True)
    parent_phone = models.CharField(max_length=15, blank=True)
    emergency_contact=models.CharField(max_length=15)
    photo=models.ImageField(upload_to='student_photos/',blank=True)
    enrollment_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    notes=models.TextField(blank=True)

    class Meta:
        ordering=['first_name','last_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - Class {self.class_level}"
    

    #The @property decorator is used in Python to make a method behave like an attribute.
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
