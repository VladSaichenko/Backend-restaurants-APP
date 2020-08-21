from rest_framework.viewsets import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from url_filter.integrations.drf import DjangoFilterBackend

from apps.food.models.ingredients import Ingredient
from apps.food.serializers.ingredients import IngredientSerializer


class IngredientView(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):

    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',
                     'calories')
