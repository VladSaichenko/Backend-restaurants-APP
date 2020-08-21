from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.main.permissions.restaurants import IsOwnerOrReadOnly
from apps.food.models.restaurants import Restaurant
from apps.food.serializers.serializers import RestaurantSerializer

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from url_filter.integrations.drf import DjangoFilterBackend


# Caching the list of restaurants for 15 minutes
@method_decorator(cache_page(60 * 15), name='list')
class RestaurantView(viewsets.ModelViewSet):

    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',
                     'address',
                     'works_from',
                     'works_until',
                     'average_dishes_price',)
