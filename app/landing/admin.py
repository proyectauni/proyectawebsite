from django.contrib import admin
from .models import Sponsor, Revista, Message

class SponsorAdmin(admin.ModelAdmin):
     list_display = ('id', 'imagen', 'nombre', 'estado')
     ordering = ('id', )
     search_fields = ('nombre', 'estado',)

class RevistaAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'link', 'estado')
    ordering = ('id', )
    search_fields = ('year', 'link',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'email', 'message', 'date_register','phone')
    ordering = ('id', )
    search_fields = ('user_name', 'message',)


# Register your models here.
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Message, MessageAdmin)