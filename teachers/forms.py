from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Teacher

class TeacherRegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=30,required=True)
    last_name=forms.CharField(max_length=30,required=True)
    email=forms.EmailField(required=True)
    phone=forms.CharField(max_length=15,required=False)
    subject=forms.CharField(max_length=100,required=False)
    qualification=forms.CharField(max_length=200,required=False)
    experience_years=forms.IntegerField(required=False,initial=0)

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def save(self,commit=True):
        user=super().save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']

        if commit:
            user.save()
            teacher=Teacher.objects.create(
                user=user,
                phone=self.cleaned_data.get('phone',''),
                subject=self.cleaned_data.get('subject'),
                qualification=self.cleaned_data.get('qualification',''),
                experience_years=self.cleaned_data.get('experience_years',0)
            )
        return user