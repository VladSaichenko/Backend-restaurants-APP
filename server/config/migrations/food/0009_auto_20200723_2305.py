# Generated by Django 3.0.8 on 2020-07-23 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_auto_20200723_0841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient_name',
            new_name='name',
        ),
    ]
