from django.shortcuts import render

from base.models import Contato
from rest_api.serializers import AgendamentoModelserializer, contatoModelSerializer
from reserva.models import reservadebanho

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from reserva.models import Petshop
from rest_api.serializers import PetshopModelSerializer



# Create your views here.
class agendamentoModelViewSet(ModelViewSet):
    queryset= reservadebanho.objects.all()
    serializer_class= AgendamentoModelserializer
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]

class contatoModelViewset(ModelViewSet):
    queryset = Contato.objects.all() 
    serializer_class= contatoModelSerializer 
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

class PetshopModelViewSet(ReadOnlyModelViewSet):   
    queryset= Petshop.objects.all()
    serializer_class= PetshopModelSerializer
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]



@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'POST':
        nome = request.data.get('nome')
        return Response({'mensahem': f'olá, {nome}!!'})
    
    
    return Response ({'Hello': 'Hello World!'})


@api_view(['GET'])
def listar_contatos(request):
    contatos = Contato.objects.all()
    contatosFormatados= []
    

    for contato in contatos:
        contatosFormatados.append({
            'nome': contato.nome,
            'email': contato.email,
            'id': contato.id
            })

    return Response ({'contatos': contatosFormatados})    

@api_view (['GET', 'PUT'])
def obter_contato_pelo_id(request,id):
    
    contato = Contato.objects.filter(id=id)
    if len(contato) == 0:
        return Response({'mensagem': 'Não foi encontrado nenhum contato com esse id'})
    
    if request.method =='PUT':
        nome= request.data.get('nome')
        email= request.data.get('email')
        mensagem = request.data.get('mensagem')

        contato[0].nome= nome
        contato[0].email= email
        contato[0].mensagem= mensagem

        contato[0].save()

        return Response({'contato': 'contato atualizado'})
    
    contatoFormatado={
        'nome': contato [0].nome,
        'email': contato [0].email,
        'mensagem': contato[0].mensagem,
        'id': contato [0].id
    }
    
    return Response({'contato': contatoFormatado})
        
    
    
    