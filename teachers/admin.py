from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'experience_years', 'phone')
    list_filter = ('subject', 'experience_years')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'subject')