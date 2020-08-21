from rest_framework.serializers import ModelSerializer
from apps.food.models.ingredients import Ingredient


class IngredientSerializer(ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'calories')
