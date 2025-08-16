from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'class_level', 'teacher', 'enrollment_date', 'is_active')
    list_filter = ('class_level', 'gender', 'is_active', 'enrollment_date')
    search_fields = ('first_name', 'last_name', 'email', 'parent_name')
    list_editable = ('is_active',)
    date_hierarchy = 'enrollment_date'