# Generated by Django 5.0.8 on 2024-08-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_jogo_palavra_alter_jogo_sequencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='jogador',
            field=models.CharField(max_length=255, verbose_name='Jogador'),
        ),
    ]
