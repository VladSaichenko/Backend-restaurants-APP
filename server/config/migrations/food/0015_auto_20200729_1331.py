# Generated by Django 3.0.8 on 2020-07-29 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0014_auto_20200729_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_dishes',
            new_name='dishes',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='coord_two',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='coord_one',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_owner',
            new_name='owner',
        ),
    ]
