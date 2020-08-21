# Generated by Django 3.0.8 on 2020-07-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='dish_ingredients',
        ),
        migrations.AddField(
            model_name='dish',
            name='dish_ingredients',
            field=models.ManyToManyField(to='food.Ingredient'),
        ),
    ]
