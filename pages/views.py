# pages/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def index(request):
    x = {
        "title": "home",
        "content": "Welcome to the home page!",
        "description": "this is a sample description for the home page.",
        "age": 12,
    }
    
    return render(request, "pages/index.html", x)

# def about(request):
#     return render(request, "pages/about.html")

def login(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     remember_me = request.POST.get('remember')
        
    #     # Authenticate user
    #     user = authenticate(request, username=username, password=password)
        
    #     if user is not None:
    #         auth_login(request, user)
            
    #         # Handle remember me functionality
    #         if not remember_me:
    #             request.session.set_expiry(0)  # Session expires when browser closes
            
    #         messages.success(request, f'Welcome back, {user.username}!')
    #         return redirect('index')  # Redirect to home page after successful login
    #     else:
    #         messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, "pages/login.html")