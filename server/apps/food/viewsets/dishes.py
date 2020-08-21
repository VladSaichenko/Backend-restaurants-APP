from rest_framework import viewsets
from apps.food.models.dish import Dish
from url_filter.integrations.drf import DjangoFilterBackend

from apps.main.permissions.dishes import AuthenticatedCreateOnlyDish
from apps.food.serializers.dish import DishSerializer


class DishView(viewsets.ModelViewSet):

    serializer_class = DishSerializer
    queryset = Dish.objects.all()

    permission_classes = (AuthenticatedCreateOnlyDish,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',
                     'total_calories',
                     'price',
                     'ingredients')
