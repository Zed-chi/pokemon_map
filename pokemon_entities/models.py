from django.db import models

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="./images", max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title