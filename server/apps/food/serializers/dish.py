from rest_framework.serializers import ModelSerializer
from apps.food.models.dish import Dish


class DishSerializer(ModelSerializer):

    class Meta:
        model = Dish
        fields = ('id',
                  'name',
                  'img',
                  'total_calories',
                  'price',
                  'ingredients')

        extra_kwargs = {'total_calories': {'read_only': True}}
