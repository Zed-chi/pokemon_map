from django.db import models


class Pokemon(models.Model):
    """ Досье на покемона """

    element_type = models.ManyToManyField("PokemonElementType", verbose_name="Элемент", blank=True)
    title_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Имя вида по-английски",
    )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Имя вида по-японски",
    )
    title_ru = models.CharField(max_length=200, verbose_name="Имя вида по-русски")
    description = models.TextField(verbose_name="Описание вида", blank=True)
    previous_evolution = models.ForeignKey(
        "self",
        verbose_name="предок",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="next_evolutions",
    )
    image = models.ImageField(
        upload_to="./images",
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Изображение",
    )
    element_type = models

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = "Покемон"
        verbose_name_plural = "Покемоны"


class PokemonEntity(models.Model):
    """ Координаты покемона """

    lat = models.FloatField(verbose_name="Широта", default=0)
    lon = models.FloatField(verbose_name="Долгота", default=0)
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.SET_NULL,
        verbose_name="покемон",
        null=True,
        related_name="entities",
    )
    appeared_at = models.DateTimeField(null=True, verbose_name="Время появления")
    disappeared_at = models.DateTimeField(null=True, verbose_name="Время исчезания")
    level = models.IntegerField(default=0, verbose_name="Уровень")
    health = models.IntegerField(default=0, verbose_name="Здоровье")
    strength = models.IntegerField(default=0, verbose_name="Сила")
    defence = models.IntegerField(default=0, verbose_name="Защита")
    stamina = models.IntegerField(default=0, verbose_name="Выносливость")

    def __str__(self):
        return f"Координаты ш:{self.lat}-д:{self.lon}"

    class Meta:
        verbose_name = "Координаты Покемона"
        verbose_name_plural = "Координаты Покемонов"


class PokemonElementType(models.Model):
    """ Элементы стихий """

    title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Название Стихии",
    )
    pokemon = models.ManyToManyField("Pokemon")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Элемент"
        verbose_name_plural = "Элементы"