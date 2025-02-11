from django.shortcuts import render

# Create your views here.
# myapp/views.py
from core_root_api.signals import order_created

def create_order(request):
    # Create the order
    user = request.user

    # Send the signal
    order_created.send(sender=Order, user=user)