from django.db import models

from apps.food.models.ingredients import Ingredient


class Dish(models.Model):
    name = models.CharField('Название блюда', max_length=250)
    img = models.ImageField('Изображение блюда')
    total_calories = models.PositiveIntegerField('Суммарная калорийность', null=True)
    price = models.PositiveIntegerField('Стоимость')
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
