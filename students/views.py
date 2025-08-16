from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student
from .forms import StudentForm

@login_required
def my_students(request):
    students = Student.objects.filter(teacher=request.user).order_by('-enrollment_date')
    return render(request, 'students/list.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.teacher = request.user
            student.save()
            messages.success(request, 'Student added successfully!')
            return redirect('my_students')
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': form})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk, teacher=request.user)
    
    if request.method == 'POST':
        if 'delete_student' in request.POST:
            student.delete()
            messages.success(request, 'Student deleted successfully!')
            return redirect('my_students')
        elif 'update_student' in request.POST:
            form = StudentForm(request.POST, request.FILES, instance=student)
            if form.is_valid():
                form.save()
                messages.success(request, 'Student updated successfully!')
                return redirect('student_detail', pk=pk)
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'students/detail.html', {'form': form, 'student': student})

