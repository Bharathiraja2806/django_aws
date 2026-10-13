from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        department = request.POST.get('department')
        salary = request.POST.get('salary')

        Data = Employee(name=name, email=email, phone=mobile, department=department, salary=salary)
        Data.save()

        return redirect('home')
    
    return render(request, 'index.html')

def view_data(request):

    employees = Employee.objects.all()
    return render(request, 'data.html', {"employees": employees})

def delete_data(request, id):

    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('view_data')

def update_dtaa(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('mobile')
        employee.department = request.POST.get('department')
        employee.salary = request.POST.get('salary')

        employee.save()
        return redirect('view_data')

    return render(request, 'update.html', {"employee": employee})