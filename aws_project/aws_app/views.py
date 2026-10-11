from django.shortcuts import render, redirect

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

        return redirect('home')
    
    return render(request, 'index.html')