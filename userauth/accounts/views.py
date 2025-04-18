from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            return render(request, 'register.html', {'error': 'User already exists'})
        User.objects.create_user(username=email, email=email, password=password)
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        elif not User.objects.filter(username=email).exists():
            return render(request, 'login.html', {'error': 'User not found'})
        else:
            return render(request, 'login.html', {'error': 'Incorrect password'})
    return render(request, 'login.html')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
