from django.core.management.base import BaseCommand
from model_bakery import baker
from reserva.models import reservadebanho

class Command(BaseCommand):
    help ='criar reservas fakes para a nossa aplicação'

    def handle(self, *args, **options):

        quantidadetotal= 100

        self.stdout.write(
            self.style.WARNING(f'gerando {quantidadetotal} reserva fakes')
        )

        for i in range(quantidadetotal):
            reserva= baker.make(reservadebanho)
            reserva.save()

            self.stdout.write(
                self.style.WARNING(f' criada a reserva de número {i + 1}')
            )

            self.stdout.write(
                self.style.SUCCESS('reserva criada com sucesso!')
            )