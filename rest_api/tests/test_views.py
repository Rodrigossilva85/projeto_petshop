import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from datetime import date, timedelta
from reserva.models import Petshop, reservadebanho


@pytest.fixture
def dados_agendamento_invalido():
    ontem = date.today() - timedelta(days=1)
    petshop = baker.make(Petshop)
    agendamento ={
       'nomedopet':'Lari',
       'telefone': '81 99997777',
       'email': 'lari@gmail.com',
       'diadareserva': ontem,
       'obsercao': '',
       'turno': 'tarde',
       'tamanho': 0,
       'petshop': petshop.pk
    }
    return agendamento

@pytest.fixture
def dados_agendamento_valido():
    hoje = date.today() + timedelta(days=1)
    petshop = baker.make(Petshop)

    agendamento = {
         
       'nomedopet':'Lari',
       'telefone': '81 99997777',
       'email': 'lari@gmail.com',
       'diadareserva': hoje,
       'obsercao': '',
       'turno': 'tarde',
       'tamanho': 0,
       'petshop': petshop.pk

    }

    return agendamento

@pytest.fixture
def agendamento_valido_instancia():
    hoje = date.today() + timedelta(days=1)
    petshop = baker.make(Petshop)

    agendamento = {
       'nomedopet':'beck',
       'telefone': '81 99997777',
       'email':'beck@gmail.com',
       'diadareserva': hoje,
       'observacao': 'beck é bonzinho',
       'turno': 'tarde',
       'tamanho': 0,
       'petshop': petshop
         

    }

    return agendamento




@pytest.fixture
def usuario():
    return baker.make('auth.User')



@pytest.mark.django_db
def test_obter_petshop_lista_vazia():
    client = APIClient ()
    resposta = client.get('/api/Petshop/')

    assert len(resposta.data['results']) == 0


@pytest.mark.django_db
def test_obter_petshops_com_1_elemento(dados_agendamento_invalido):
    client = APIClient()
    
    resposta = client.get('/api/Petshop/', dados_agendamento_invalido)

    assert len(resposta.data['results']) == 1


@pytest.mark.django_db
def test_criar_agendamento(dados_agendamento_valido, usuario):  
    client = APIClient()
    client.force_authenticate(usuario)  
    resposta = client.post('/api/agendamento/', dados_agendamento_valido)

    assert resposta.status_code == 201

@pytest.mark.django_db
def test_obter_agendamento_pelo_id(agendamento_valido_instancia):

    reservadebanho.objects.create(**agendamento_valido_instancia)    
    client = APIClient()
    resposta = client.get('/api/agendamento/1/')

    assert resposta.json()['nomedopet']== 'beck'
    assert resposta.json()['email'] == 'beck@gmail.com'
    assert resposta.json()['turno'] == 'tarde' 
    assert resposta.status_code == 200


@pytest.mark.django_db
def test_remover_agendamento_pelo_id(agendamento_valido_instancia, usuario):

    reservadebanho.objects.create(**agendamento_valido_instancia)    
    client = APIClient()
    client.force_authenticate(usuario)

    respostaprimeiroget = client.get('/api/agendamento/1/')

    assert respostaprimeiroget.json()['nomedopet']== 'beck'
    assert respostaprimeiroget.status_code == 200    

    client.delete('/api/agendamento/1/')
    respostasegundoget = client.get('/api/agendamento/1/')

    assert respostasegundoget.status_code == 404