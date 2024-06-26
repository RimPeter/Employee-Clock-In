from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'employee_app/index.html')


def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'employee_app/my-login.html', context)    

def my_logout(request):
    auth.logout(request)
    return redirect('my-login')  

@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'employee_app/dashboard.html')      