# Generated by Django 3.2.3 on 2021-07-23 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='money',
            old_name='salary',
            new_name='price',
        ),
    ]
