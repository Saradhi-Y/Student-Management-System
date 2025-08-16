from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_students, name='my_students'),
    path('add/', views.add_student, name='add_student'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
]