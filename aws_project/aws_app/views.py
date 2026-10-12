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