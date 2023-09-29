from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from reserva.models import reservadebanho
from base.models import Contato
from reserva.models import Petshop


class PetshopModelSerializer(ModelSerializer):

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

    petshop =PetshopRelatedFieldCustomSerializer(queryset= Petshop.objects.all(), read_only=False)
    
    class Meta:
    
        model =reservadebanho
        fields ='__all__'

class contatoModelSerializer(ModelSerializer):
    class Meta:

        model= Contato
        fields ='__all__'      

