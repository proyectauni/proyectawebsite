from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "landing/home.html")

def about(request):
    return render(request, "landing/about-me.html")

def contacto(request):
    return render(request, "landing/contactame.html")