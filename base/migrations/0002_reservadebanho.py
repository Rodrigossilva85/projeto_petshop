# Generated by Django 4.2.3 on 2023-08-12 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservadebanho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomedopet', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('diadareserva', models.DateField()),
                ('observacao', models.TextField(blank=True)),
            ],
        ),
    ]
