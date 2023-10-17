from typing import Any
from django.core.management.base import BaseCommand
from reserva.models import reservadebanho, Petshop
import random

class Command(BaseCommand):
    help ='sorteia uma qauntidade x de reseva de forma automatica'
    
    def list_petshop(self):
        return Petshop.objects.all().values_list('pk', flat= True)
    
    def add_arguments(self, parser):

        parser.add_argument(
        'quantity',
        nargs = '?',
        default= 5,
        type= int,
        help= 'quantidade de reservas a serem sorteada'
        )

        parser.add_argument(
            '-petshop',
            required= True,
            type= int,
            choices = self.list_petshop(),
            help ='id do petshop para sortear as reservas'
        )    

    def handle(self, *args: Any, **options: Any):
        quantity = options['quantity']
        petshop_id = options['petshop']
        reservas = reservadebanho.objects.filter(petshop = petshop_id)
        reservas_escolhidas = self.escolher_reservas(reservas, quantity)
        self.stdout.write(
            self.style.SUCCESS('O sorteio foi concluído com sucesso!')
        )
        self.imprimir_petshop(petshop_id)
        self.imprimir_reservas_selecionadas(reservas_escolhidas)
    
    
    def imprimir_reservas_selecionadas(self,reservas):
        self.stdout.write(
            self.style.HTTP_INFO('reservas selecionadas!')
        )
        for reserva in reservas:
            self.stdout.write(
            self.style.HTTP_INFO(str(reserva))
            )
            
            self.stdout.write()
   
   
    def imprimir_petshop(self, petshop_id):
        self.stdout.write(
            self.style.HTTP_INFO('dados do petshop que foi sorteado as reservas!')
        )
        petshop = Petshop.objects.get(pk=petshop_id)
        self.stdout.write(str(petshop))


    def escolher_reservas(self,lista_de_reservas_query_set, quantity):
        lista_de_reserva_list = list(lista_de_reservas_query_set)

        if quantity > len(lista_de_reserva_list):
            quantity = len(lista_de_reserva_list)

        return random.sample(lista_de_reserva_list, quantity)
    
