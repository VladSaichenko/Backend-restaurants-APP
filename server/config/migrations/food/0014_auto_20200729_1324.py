# Generated by Django 3.0.8 on 2020-07-29 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_auto_20200724_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='dish_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='dish_ingredients',
            new_name='ingredients',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='dish_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='dish_total_calories',
            new_name='total_calories',
        ),
    ]
