from rest_framework import routers

from apps.test.viewsets import TestViewSet
from apps.users.viewsets.views import UserViewSet
from apps.food.viewsets.views import RestaurantView
from apps.food.viewsets.ingredients import IngredientView
from apps.food.viewsets.dishes import DishView


router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('users', UserViewSet, basename='users')
router.register('places', RestaurantView, basename='place')
router.register('ingredients', IngredientView, basename='ingredient')
router.register('dishes', DishView, basename='dish')
