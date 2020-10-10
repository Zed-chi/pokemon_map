# Generated by Django 2.2.3 on 2020-10-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0007_auto_20201010_1159"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemon",
            name="description",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="Описание вида"
            ),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="title_en",
            field=models.CharField(
                blank=True,
                default="",
                max_length=200,
                null=True,
                verbose_name="Имя вида по-английски",
            ),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="title_jp",
            field=models.CharField(
                blank=True,
                default="",
                max_length=200,
                null=True,
                verbose_name="Имя вида по-японски",
            ),
        ),
    ]
