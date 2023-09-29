from django.shortcuts import render
from reserva.forms import ReservadebanhoForm

# Create your views here.

def criar_reserva_banho(request):
    
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
