# Generated by Django 3.0.8 on 2020-07-23 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20200723_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_ingredients',
            field=models.ManyToManyField(related_name='Ingredient', to='food.Ingredient'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_total_calories',
            field=models.PositiveIntegerField(null=True, verbose_name='Суммарная калорийность'),
        ),
    ]
