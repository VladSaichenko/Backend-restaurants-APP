from django.db import models


class Ingredient(models.Model):
    name = models.CharField('Ингредиент', max_length=250)
    calories = models.IntegerField('Калорийность')

    def __str__(self):
        return self.name
