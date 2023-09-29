from django import forms
from reserva.models import reservadebanho
from datetime import date

class ReservadebanhoForm(forms.ModelForm):
    
    class Meta:
        model = reservadebanho
        fields = ['nomedopet', 'telefone','email', 'diadareserva', 'turno','tamanho','observacao','petshop']
        
        
        widgets = {
            'diadareserva': forms.DateInput(attrs={'type':'date'}),
        
        }

    def clean_diadareserva(self):
        diadareservaselecionada= self.cleaned_data['diadareserva']
        hoje= date.today()

        if diadareservaselecionada < hoje:
            raise forms.ValidationError('Não é possivél reservar para uma data no Passado!')
        
        quantidadedereservasparaodiaselecionado= reservadebanho.objects.filter(diadareserva= diadareservaselecionada).count()

        if quantidadedereservasparaodiaselecionado>=4:

            raise forms.ValidationError('O Limite Máximo de reservas para este dia já foi atingido. escolha outra data. ')

        return diadareservaselecionada      