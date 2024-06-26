from django.shortcuts import render
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .forms import LoginForm

def home(request):
    #return HttpResponse('Hello, Django!')
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
                #return redirect('home')
    context = {'form': form}
    return render(request, 'employee_app/my-login.html', context)            