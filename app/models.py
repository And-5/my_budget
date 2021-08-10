from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone

class Money (models.Model):
    CHOISES_CATEGORY = (
        ('Продукты', 'Продукты'),
        ('Одежда', 'Одежда'),
        ('Машина', 'Машина'),
    )
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=150, choices=CHOISES_CATEGORY, default='Продукты')
    # id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def _price_sum(self):
        return self.objects.aggregate(total_price=Sum('price'))['total_price']

    price_sum = property(_price_sum)

