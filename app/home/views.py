from django.shortcuts import render

# Create your views here.
def home(request):
    # patrocinador = Patrocinador.objects.all()
    return render(request, "home/home.html")