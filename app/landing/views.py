from django.shortcuts import render
#importar modelos
from .models import *

# Create your views here.
def home(request):

    all_sponsors = Sponsor.objects.filter(estado = True)

    print (all_sponsors[0])

    return render(request, "landing/home.html",{'all_sponsors' : all_sponsors})

def about(request):
    return render(request, "landing/about-me.html")

def contacto(request):
    return render(request, "landing/contactame.html")