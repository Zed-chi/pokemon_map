# Generated by Django 2.2.3 on 2020-10-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_pokemonelementtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonelementtype',
            name='pokemon',
            field=models.ManyToManyField(related_name='elements', to='pokemon_entities.Pokemon'),
        ),
    ]
