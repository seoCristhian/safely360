from django.urls import path, include
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', vistaInscripcion, name='archivo'),
    path('360/', include('paypal.standard.ipn.urls')),
]
