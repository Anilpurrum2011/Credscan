from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'scanner/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'scanner/login.html', {'error': 'Invalid credentials'})
    return render(request, 'scanner/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'scanner/profile.html', {'profile': user_profile})