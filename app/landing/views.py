from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
#importar modelos
from .models import Sponsor, Revista, Message

# Create your views here.
def home(request):

    all_sponsors = Sponsor.objects.filter(estado = True)

    print (all_sponsors[0])

    return render(request, "landing/home.html",{'all_sponsors' : all_sponsors})

def about(request):
    return render(request, "landing/about-me.html")

def contacto(request):
    return render(request, "landing/contactame.html")

def directiva(request):

    all_sponsors = Sponsor.objects.filter(estado = True)

    print (all_sponsors[0])

    return render(request, "landing/directiva.html",{'all_sponsors' : all_sponsors})

def sendMail(request):
    if request.method is "GET":
        all_sponsors = Sponsor.objects.filter(estado = True)
        return render(request, "landing/home.html",{'all_sponsors' : all_sponsors})

    else:
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        message = request.POST.get('message', "")
        phone = request.POST.get('phone', "")
        messages = Message.objects.create(user_name=name, email=email, message=message, phone=phone)
        messages.save()
        msg_html_prospect = render_to_string('mail/usuario.html', {"message": messages})
        send_mail("Gracias por contactarnos! :)", '', 'proyecta@uni.edu.pe',
                  [messages.email],
                  html_message=msg_html_prospect, )

        auto_msg_html = render_to_string('mail/administrador.html', {"message": messages})
        send_mail('Nuevo Contacto', '', 'proyecta@uni.edu.pe',
                  ['proyecta@uni.edu.pe'],
                  html_message=auto_msg_html, )
        return redirect("home")

        # print(request.body)
        # return render(request, "landing/contactame.html")

def proyectos(request):
    
    return render(request, "landing/proyectos.html")

    

