from django.urls import path
from app.views import *

urlpatterns = [
    path('', index),
    path('index', index),
    path('registration', registration),
    path('login', login_users),
    path('logout', do_logout),
    path('register', register),
    path('log_2', login_1),
    path('delete/<int:id>', delete),
]