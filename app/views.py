import requests
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseNotFound
from app.models import *
from .forms import MoneyForm
from django.db.models import Sum
from django.db.models.functions import Coalesce

def index(request):
    error = ''
    if request.method == 'POST':
        form = MoneyForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/')
        else:
            error = 'Ошибка в заполнении'
    form = MoneyForm()
    # money = Money.objects.filter(user=request.user.id, category='Машина')
    money = Money.objects.filter(user=request.user.id)
    # price_sum = money.values('price')
    price_sum = money.values_list('price', flat=True)
    price_sum_s = sum(price_sum)

    context = {
        'price_sum_s': price_sum_s,
        'price_sum': price_sum,
        'form': form,
        'error': error,
        'money': money,
    }
    return render(request, 'index.html', context)

def registration(request):
    return render(request, 'registration.html')

def login_users(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render(request, 'error.html', {})
    else:
        login(request, user)
        return HttpResponseRedirect('/')

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')

def register(request):
    user = User.objects.create_user(
        request.POST['login'],
        password=request.POST['password'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email']
    )
    login(request, user)
    return HttpResponseRedirect('index')

def login_1(request):
    if User.objects.filter(username=request.POST['aaa']):
        exists = 'n'
    else:
        exists = 'y'
    response = {
        'exists': exists
    }
    return JsonResponse(response)

def delete(request, id):
    try:
        money = Money.objects.get(id=id)
        money.delete()
        return HttpResponseRedirect('/')
    except Money.DoesNotExist:
        return HttpResponseNotFound('<h2>Money not found</h2>')
