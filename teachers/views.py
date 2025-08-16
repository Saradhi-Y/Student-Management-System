
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TeacherRegistrationForm
from students.models import Student
from django.contrib.auth import logout

def register_view(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teachers/register.html', {'form': form})

@login_required
def dashboard_view(request):
    students = Student.objects.filter(teacher=request.user).order_by('-enrollment_date')
    context = {
        'students': students,
        'total_students': students.count(),
        'active_students': students.filter(is_active=True).count(),
        'recent_students': students[:5]
    }
    return render(request, 'teachers/dashboard.html', context)

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')