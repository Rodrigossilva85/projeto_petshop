from django import forms
from base.models import Contato
from base.models import reservadebanho



class ContatoForm(forms.ModelForm):

   class Meta:
       model = Contato
       fields = ['nome', 'email', 'mensagem']



class ReservadebanhoForm(forms.ModelForm):
    
    class Meta:
        model = reservadebanho
        fields = ['nomedopet', 'telefone', 'diadareserva', 'observacao']
        
        
        widgets = {
            'diadareserva': forms.DateInput(attrs={'type':'date'}),
        
        }

    


    
          
        