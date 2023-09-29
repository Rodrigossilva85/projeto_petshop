# Generated by Django 4.2.3 on 2023-09-14 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_alter_reservadebanho_diadareserva_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome do petshop')),
                ('endereco', models.CharField(max_length=50, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
            ],
        ),
        migrations.AddField(
            model_name='reservadebanho',
            name='petshop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='reserva.petshop'),
        ),
    ]
