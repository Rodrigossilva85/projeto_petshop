from pytest_django.asserts import assertTemplateUsed
from datetime import date, timedelta
import pytest
from model_bakery import baker
from reserva.models import reservadebanho

@pytest.mark.django_db
def test_reserva_deve_retornar_template_correta(client):

    response = client.get('/reserva/criar/')

    assert response.status_code == 200
    assertTemplateUsed(response,'reserva_de_banho.html')


@pytest.fixture
def reserva_valida():
    data= date.today() + timedelta(days=1)
    dados={
       'nomedopet':'liz',
       'telefone': '8199997777',
       'email': 'liz@gmail.com',
       'diadareserva': data,
       'observacao': 'liz está bastante suja!',
       'turno': 'tarde',
       'tamanho': 2
    }
    return dados


@pytest.mark.django_db
def test_reserva_criada_com_sucesso(client, reserva_valida):
   
    response = client.post('/reserva/criar/', reserva_valida)
    assert response.status_code == 200
    assert 'Reserva foi enviada com sucesso!' in str(response.content)
    
    
@pytest.fixture
def reserva_invalida():
    data= date.today() - timedelta(days=1)
    dados={
       'nomedopet':'liz',
       'telefone': '8199997777',
       'email': 'liz@gmail.com',
       'diadareserva': data,
       'observacao': 'liz está bastante suja!',
       'turno': 'tarde',
       'tamanho': 2
    }
    return dados



@pytest.mark.django_db
def reserva_invalida(client, reserva_invalida):
    
    response = client.post('/reserva/criar/', reserva_invalida)
    assert response.status_code == 200
    assert 'Nao e possivel reservar para uma data no Passado!' in str(response.content)

@pytest.mark.django_db
def test_reserva_limite_maximo_atingido(client, reserva_valida):
    amanha = date.today() + timedelta(days=1)
    quantidade = 5
    baker.make (
        reservadebanho,
        quantidade,
        diadareserva = amanha
    )    
    
    response = client.post('/reserva/criar/', reserva_valida)

    assert response.status_code == 200
    assert 'O Limite Maximo de reservas para este dia ja foi atingido. escolha outra data.' in str(response.content)  


@pytest.mark.django_db
def test_se_reserva_esta_inserindo_no_banco_corretamente(client, reserva_valida):

    client.post('/reserva/criar/', reserva_valida)

    assert reservadebanho.objects.all().count() == 1

    primeirareservanobanco = reservadebanho.objects.first()
    print(primeirareservanobanco)

    assert primeirareservanobanco.nomedopet == reserva_valida ['nomedopet']
    assert primeirareservanobanco.diadareserva == reserva_valida ['diadareserva']
    assert primeirareservanobanco.turno == reserva_valida ['turno']












    
   
    