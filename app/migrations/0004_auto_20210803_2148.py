# Generated by Django 3.2.3 on 2021-08-03 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_money_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='money',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
