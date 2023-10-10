from rest_framework.serializers import (
ModelSerializer,
PrimaryKeyRelatedField, 
HyperlinkedRelatedField, 
ValidationError)
from reserva.models import reservadebanho
from base.models import Contato
from reserva.models import Petshop
from datetime import date


class PetshopModelSerializer(ModelSerializer):

    reserva = HyperlinkedRelatedField(
        many = True,
        read_only =True,
        view_name = 'api: reserva-detali'
    )

    class Meta:

        model= Petshop
        fields = '__all__'    
    

class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self,**kwargs):
        self.serializer= PetshopModelSerializer
        super().__init__(**kwargs)
    
    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context= self.context).data


class AgendamentoModelserializer(ModelSerializer):

    petshop =PetshopRelatedFieldCustomSerializer(
        queryset = Petshop.objects.all(),
        read_only=False
    )
    def validate_diadareserva(self, value):

        hoje = date.today()
        if value < hoje :
            raise ValidationError ('nao e permitido agendamento com data do passado')
        return value



    class Meta:
    
        model =reservadebanho
        fields ='__all__'

class contatoModelSerializer(ModelSerializer):
    class Meta:

        model= Contato
        fields ='__all__'      

