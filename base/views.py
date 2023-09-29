
from django.shortcuts import render
from django.http import HttpResponse
from base.forms import ContatoForm
from base.forms import ReservadebanhoForm
from base.models import Contato

#Create your views here.
def inicio (request):
    return render(request, 'inicio.html')



def contato (request):
    print("método:", request.method)
    sucesso = False

    
    form = ContatoForm(request.POST or None)  
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        mensagem = form.cleaned_data['mensagem']

        Contato.objects.create (nome=nome, email=email, mensagem=mensagem)
        sucesso = True


    context ={
        "Nome": "FABIO MARIANO",
        "Telefone": "81 99999999",
        "form": form,
        "sucesso": sucesso
    }
    return render(request, 'contato.html', context)


def reservadebanho(request):
    
    sucesso = False
    
    form = ReservadebanhoForm (request.POST  or None)
    if form.is_valid():
        form.save()
        sucesso = True
    
    
    context ={
        "form": form,
        "sucesso": sucesso
    }        
    return render(request,"reserva_de_banho.html", context)    