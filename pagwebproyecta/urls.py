"""pagwebproyecta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.landing import views as landing_views
#para la imagen
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', landing_views.home, name="home"),
    path('directiva/', landing_views.directiva, name="directiva"),
    path('proyectos/', landing_views.proyectos, name="proyectos"),
    path('about-me/',landing_views.about, name="about"),
    path('contactame/',landing_views.contacto, name="contacto"),
    path('admin/', admin.site.urls),
    # Paths de Auth (para la autenticación)
    path('accounts/', include('django.contrib.auth.urls')),
    path('correoproyecta/', landing_views.sendMail, name="correo")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)