from .models import Login
from django.shortcuts import render


def user_login(request):
    if request.method == "POST":
        username_v = request.POST.get('username')
        password_v = request.POST.get('password')
        if username_v and password_v:
            data = Login(username=username_v, password=password_v)
            data.save()
    return render(request, "users/Login.html")
def profile(request):
    # username_v = request.POST.get('username')
    # password_v = request.POST.get('password')
    # data = Login.objects.filter(username=username_v, password=password_v).first()
    # if data:
        return render(request, "users/profile.html")
    # else:
    #     return render(request, "users/login.html", {"error": "Invalid credentials"})