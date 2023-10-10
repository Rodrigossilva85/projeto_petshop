
from rest_framework.test import APIClient
from model_bakery import baker
from datetime import date, timedelta
from reserva.models import Petshop
from rest_api.serializers import AgendamentoModelserializer
from pytest import mark, fixture


@fixture
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

@mark.django_db
def  test_agendamento_invalido(dados_agendamento_invalido):
    
    
    serializer = AgendamentoModelserializer(data= dados_agendamento_invalido)
    assert not serializer.is_valid()
