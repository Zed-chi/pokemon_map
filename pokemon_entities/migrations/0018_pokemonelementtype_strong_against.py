# Generated by Django 2.2.3 on 2020-10-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0017_pokemonelementtype_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonelementtype',
            name='strong_against',
            field=models.ManyToManyField(to='pokemon_entities.PokemonElementType', verbose_name='Используется против'),
        ),
    ]