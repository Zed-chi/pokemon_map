from django.db import models

# your models here
class Pokemon(models.Model):
    title_en = models.CharField(max_length=200, default="")
    title_jp = models.CharField(max_length=200, default="")
    title_ru = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
    previous_evolution = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="previous",
    )
    next_evolution = models.ForeignKey(
        "self",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="next",
    )
    image = models.ImageField(
        upload_to="./images", max_length=100, null=True, blank=True
    )

    def __str__(self):
        return self.title_en


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True)
    appeared_at = models.DateTimeField(auto_now=True)
    disappeared_at = models.DateTimeField(auto_now=True)
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.lat}-{self.lon}"
