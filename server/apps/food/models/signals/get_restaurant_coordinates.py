from django.db.models.signals import pre_save
from django.dispatch import receiver

from yandex_geocoder import Client, YandexGeocoderException

from apps.food.models.restaurants import Restaurant


@receiver(pre_save, sender=Restaurant)
def get_restaurant_coordinates(sender, instance, **kwargs):
    if not (instance.longitude and instance.latitude):
        try:
            client = Client('1934adac-bcef-4dc3-8f39-a57fc22c1b52')
            instance.longitude, instance.latitude = client.coordinates(instance.address)
        except YandexGeocoderException:
            instance.longitude, instance.latitude = (-1, -1)
