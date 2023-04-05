from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from paypal.standard.models import ST_PP_COMPLETED
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

def vistaInscripcion(request):
    if request.method == 'POST':
        form = UsuarioFormSafely(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'venta.html')
    else:
        form = UsuarioFormSafely()
    return render(request, 'documentoSeguridad.html', {'form': form})

def checkout(request):
    # Aquí debes crear un objeto que represente la orden, que incluya información como el monto, la descripción, etc.
    # Después, crea una instancia de PayPalPaymentsForm con los datos de la orden
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "100.00",  # Aquí debes poner el monto de la orden
        "currency_code": "USD",  # Aquí debes poner la moneda de la orden
        "item_name": "Mi orden",  # Aquí debes poner el nombre de la orden
        "invoice": "123456",  # Aquí debes poner el número de factura o la identificación de la orden
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('paypal_return')),
        "cancel_return": request.build_absolute_uri(reverse('home')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'checkout.html', {'form': form})









