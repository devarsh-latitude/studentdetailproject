from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Student
from .forms import StudentForm
# Create your views here.
def home(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    students=Student.objects.all()
    return render(request,'home.html',{'student_form':form,'students':students})

def delete_data(request,pk):
    student=Student.objects.get(pk=pk)
    student.delete()
    return redirect('home')

def update_data(request,pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'update.html',{'student_form':form})