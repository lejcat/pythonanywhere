# accounts/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', index, name='home'),
]