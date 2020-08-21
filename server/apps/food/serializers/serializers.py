from rest_framework import serializers

from apps.food.models.restaurants import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('id',
                  'name',
                  'address',
                  'works_from',
                  'works_until',
                  'img',
                  'average_dishes_price',
                  'longitude',
                  'latitude',
                  'owner',
                  'dishes')

        extra_kwargs = {'average_dishes_price': {'read_only': True},
                        'owner': {'read_only': True},
                        'longitude': {'read_only': True},
                        'latitude': {'read_only': True}}
