from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, "users/Login.html")

@login_required
def profile(request):
    return render(request, "users/profile.html")

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('index')