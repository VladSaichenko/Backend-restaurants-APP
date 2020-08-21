from django.db import models
from django.contrib.auth.models import User

from apps.food.models.dish import Dish


class Restaurant(models.Model):
    # Set by user
    name = models.CharField('Название заведения', max_length=250)
    address = models.CharField('Адрес заведения', max_length=250)
    works_from = models.TimeField(verbose_name='Работает с:')
    works_until = models.TimeField(verbose_name='Работает до:')
    img = models.ImageField('Изображение заведения', null=True)

    # Automatically set
    average_dishes_price = models.IntegerField('Средняя стоимость блюда', null=True)
    longitude = models.DecimalField('Longitude', max_digits=18, decimal_places=3)
    latitude = models.DecimalField('Latitude', max_digits=18, decimal_places=3)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish, blank=True)

    def __str__(self):
        return self.name
