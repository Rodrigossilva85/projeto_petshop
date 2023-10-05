import pytest
from reserva.models import reservadebanho, Petshop
from model_bakery import baker
from datetime import date

@pytest.fixture
def reserva():

    data = date(2023,10,29)
    reserva = baker.make(
     reservadebanho,
     nomedopet = 'pingo',
     diadareserva = data,
     turno = 'tarde',
     email = 'gabigralato@gmail.com',
     observacao ='pingo fica muito agitado no banho!',
     tamanho= 2
    )
    return reserva



def test_config():

    assert 1 == 1



@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva):
    
    assert str(reserva)== 'Nome do pet: pingo - Dia da reserva: 2023-10-29 - Turno: tarde'
    assert reserva.email == 'gabigralato@gmail.com'
    

@pytest.mark.django_db
def test_campos_observacao_e_tamanho_de_reserva(reserva):

    assert reserva.observacao =='pingo fica muito agitado no banho!'
    assert reserva.tamanho == 2


@pytest.mark.django_db
def test_quantidade_de_reserva_do_pestshop():  

    petshop = baker.make(Petshop)
    quantidade = 5

    baker.make(
        reservadebanho,
        quantidade,
        petshop = petshop
    )
    assert petshop.quantidade_reservas() == 5


