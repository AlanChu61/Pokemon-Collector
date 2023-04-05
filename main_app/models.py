from django.db import models
from django.urls import reverse


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    pokmon_id = models.IntegerField(default=0)
    img = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pokemon_detail', kwargs={'pokemon_id': self.id})
