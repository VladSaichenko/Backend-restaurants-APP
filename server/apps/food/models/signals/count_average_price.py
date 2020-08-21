from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from apps.food.models.restaurants import Restaurant


@receiver(m2m_changed, sender=Restaurant.dishes.through)
def count_average_price(sender, instance, **kwargs):
    a = Restaurant.objects.get(id=instance.id)
    dishes_list = a.dishes.all()
    s = 0
    for dish in dishes_list:
        s += dish.price
    try:
        a.average_dishes_price = s/len(dishes_list)
    except ZeroDivisionError:
        a.average_dishes_price = 0
    a.save()
