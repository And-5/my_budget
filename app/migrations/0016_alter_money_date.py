# Generated by Django 3.2.3 on 2021-08-08 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_money_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
