# Generated by Django 3.0.8 on 2020-07-22 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20200722_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_dishes',
            field=models.ManyToManyField(related_name='Dish', to='food.Dish'),
        ),
    ]
