from django.shortcuts import render
import mpesa

from .models import *

# Create your views here.

def index(request):
    products = Products.objects.all()[:10]
    context = {"products":products}
    return render(request,"index.html",context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_item":0,"get_cart_total":0}
    context = {"items":items,"order":order}
    return render(request,"cart.html",context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_items":0,"get_cart_total":0}
    context = {"items":items,"order":order}
    return render(request,"checkout.html",context)

