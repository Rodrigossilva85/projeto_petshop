# Generated by Django 4.2.3 on 2023-08-16 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_contato_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='lido',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]