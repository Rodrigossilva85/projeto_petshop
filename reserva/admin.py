from django.contrib import admin
from reserva.models import reservadebanho

# Register your models here.
@admin.register(reservadebanho)

class reservadebanhoadmin(admin.ModelAdmin):

    list_display = ['nomedopet','email','diadareserva','turno','tamanho','observacao']
    search_fields= ['nomedopet','email']
    list_filter = ['diadareserva','turno','tamanho']