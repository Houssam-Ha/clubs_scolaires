# pages/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def index(request):
    return render(request, "pages/index.html", )


