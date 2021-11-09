from django.shortcuts import render
import mpesa
from django.http import JsonResponse
import json

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
        order = {"get_cart_items":0,"get_cart_total":0}
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
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action',action)
    print('productId',productId)

    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == "add":
        orderItem.qty = (orderItem.qty + 1)
    elif action == "remove":
        orderItem.qty = (orderItem.qty - 1)
        orderItem.save()
        
    if orderItem.qty <= 0:
        orderItem.delete()


    return JsonResponse('Item was added',safe=False)

def Login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

