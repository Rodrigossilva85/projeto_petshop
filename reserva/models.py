from django.db import models

# Create your models here.
class reservadebanho(models.Model):

    tamanho_opcoes= (
        (0,'Pequeno'),
        (1,'Médio'),
        (2,'Grande')
    )
    
    turno_opcoes = (
        ('manha','Manhã'),
        ('tarde','Tarde'),
        ('noite', 'Noite')
    )
    
    
    nomedopet= models.CharField(verbose_name='Nome do Pet',max_length=50)
    telefone= models.CharField(verbose_name='Telefone',max_length=15)
    email= models.EmailField(verbose_name='E-Mail',max_length=75)
    diadareserva= models.DateField(verbose_name='Dia da Reserva')
    observacao= models.TextField(verbose_name='Observações',blank=True) 
    turno= models.CharField(verbose_name='Turno',max_length=5, choices= turno_opcoes)
    tamanho= models.IntegerField(verbose_name='Tamanho',choices= tamanho_opcoes)
    petshop= models.ForeignKey('Petshop', related_name='reservas', on_delete= models.CASCADE ,blank=True, null=True)

    class Meta:
        verbose_name= 'Formulário de Reserva de Banho'
        verbose_name_plural= ' Formulários de Reservas de Banhos'

class Petshop(models.Model):
    nome= models.CharField(verbose_name="nome do petshop", max_length=50)
    endereco= models.CharField(verbose_name='Endereço', max_length=50)
    telefone= models.CharField(verbose_name='Telefone',max_length=15)
    def __str__(self):
        return f'Loja: {self.nome} - Endereço: {self.endereco} - Telefone: {self.telefone}'

