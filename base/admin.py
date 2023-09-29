from django.contrib import admin
from django.contrib import messages
from base.models import Contato


# Register your models here.


@admin.action(description='Marcar formulário de contatos selecionados como lido')

def marcar_como_lido(modeladmin,request,queryset):

    queryset.update(lido=True)
    modeladmin.message_user( request,'Os formulários de contatos foram marcados como lido!', messages)


@admin.action(description='Marcar formulário de contatos selecionados como não lido')
def marcar_como_nao_lido(modeladmin,request,queryset):

    queryset.update(lido= False)
    modeladmin.message_user( request,'Os formulários de contatos foram marcados como não lido!', messages)

@admin.register(Contato)
class contatoadmin(admin.ModelAdmin):
    
    list_display = ['nome','email','mensagem','data','lido']
    search_fields = ['nome', 'email']
    list_filter = ['data' ,'lido']
    actions = [marcar_como_lido, marcar_como_nao_lido]

   
    