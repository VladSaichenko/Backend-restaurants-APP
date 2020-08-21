from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from apps.food.models.dish import Dish


@receiver(m2m_changed, sender=Dish.ingredients.through)
def count_total_calories(sender, instance, **kwargs):
    a = Dish.objects.get(id=instance.id)
    ingredients_list = a.ingredients.all()
    s = 0
    for ingredient in ingredients_list:
        s += ingredient.calories

    a.total_calories = s
    a.save()
