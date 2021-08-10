from django.forms import ModelForm, TextInput, DateInput
from .models import *

class MoneyForm(ModelForm):
    class Meta:
        model = Money
        fields = ['name', 'price', 'date', 'category']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Наименование'
            }),
            'date': DateInput(attrs={
                'placeholder': 'Дата добавления'
            })
        }