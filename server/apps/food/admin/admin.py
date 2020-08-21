from django.contrib import admin
from apps.food.models.restaurants import Restaurant
from apps.food.models.ingredients import Ingredient
from apps.food.models.dish import Dish


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'img',
        'owner',
        'works_from',
        'works_until',
    )

    readonly_fields = (
        'average_dishes_price',
        'longitude',
        'latitude',
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'calories',
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'img',
        'price',
    )

    readonly_fields = (
        'total_calories',
    )
