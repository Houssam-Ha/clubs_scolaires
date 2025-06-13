from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    x = {
        "title": "home",
        "content": "Welcome to the home page!",
        "description": "this is a sample description for the home page.",
        "age": 12,
    }
    
    return render(request, "pages/index.html", x)

def about(request):
    return render(request, "pages/about.html")
