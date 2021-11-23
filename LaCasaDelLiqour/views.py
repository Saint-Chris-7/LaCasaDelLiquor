from django.shortcuts import render,redirect
import mpesa
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib import messages
from .forms import ShippingAddressForm
# Create your views here.

def index(request):
    wines = Products.objects.filter(category="Wine")
    whiskeys = Products.objects.filter(category="Whiskey")
    rums = Products.objects.filter(category="Rum")
    vodkas = Products.objects.filter(category="Vodka")
    gins = Products.objects.filter(category="Gin")
    beers = Products.objects.filter(category="Beer")
    Product = [items for items in Products.objects.all()] 
    
    item_name = request.GET.get("search")
    if item_name != '' and item_name is not None:
        item_name = Products.objects.filter(name_icontains=item_name)
    context = {"wines":wines,"whiskeys":whiskeys,"rums":rums,"vodkas":vodkas,"gines":gins,"beers":beers,"item_name":item_name,"Product":Product}
    return render(request,"index.html",context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItem = Order.get_cart_items
    else:
        items = []
        cartItem = Order['get_cart_items']
        order = {"get_cart_items":0,"get_cart_total":0}
    context = {"items":items,"order":order,"cartItem":cartItem}
    return render(request,"cart.html",context)
"""
    this is the checkout view
"""
def checkout(request):
    if request.user.is_authenticated:
        forms = ShippingAddressForm()
        if request.method == "POST":
            forms = ShippingAddressForm(request.POST)
            if forms.is_valid():
                forms.save()
        else:
            forms = ShippingAddressForm()
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItem = Order.get_cart_items
    else:
        items = []
        cartItem = Order['get_cart_items']
        order = {"get_cart_items":0,"get_cart_total":0}
    context = {"items":items,"order":order,"cartItem":cartItem,"forms":forms}
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
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)
        orderItem.save()
        
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added',safe=False)









#authentication functions

def Login(request):
    if request.method == "POST":
        UserName = request.POST['Uname']
        password1 = request.POST['Password1']
        user = authenticate(request,username=UserName,password=password1)
        if user is not None:
            login(request,user)
            messages.info(request,"welcome {}".format(user.get_username()))
            return redirect("/")
        else:
            messages.info(request,"invalid user try again or sign-up")
            return redirect("login") 
    return render(request,"login.html")

#logout
def Logout(request):
    logout(request)
    return render(request,"logout.html")


def signup(request):
    if request.method == "POST":
        FirstName = request.POST['Fname']
        LastName = request.POST['Lname']
        UserName = request.POST['Uname']
        Email = request.POST['Email']
        Password1 = request.POST['Password1']
        Password2 = request.POST['Password2']

        if Password1 == Password2:
            if User.objects.filter(username=UserName).exists():
                messages.info(request,"username already exist, try another username")
            elif User.objects.filter(email=Email).exists():
                messages.info(request,"email already in use")
            else:
                user=User.objects.create(username=UserName,email=Email,password=Password1,first_name=FirstName,last_name=LastName)
                user.save();
                messages.success(request,"Congratualation! Your accout has been created succesfully")
                return redirect("login")
                
        else:
            messages.info(request,"incorrect password")
            
    else:
        return render(request,"signup.html")



#generating automating login email.
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def succes(request):
    template = render_to_string("email_resp.html",{"fname":request.user.customer.first_name})
    email = EmailMessage(
        'Welcome new customer',
        'template',
        settings.EMAIl_HOST_USER,
        ['request.user.customer.email']#the email of receivers.
    )
    email.fail_silently = False
    email.send()


