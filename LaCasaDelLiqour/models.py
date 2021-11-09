from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    img = models.ImageField(upload_to="media")
    name = models.CharField(max_length=20)
    qty = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
        
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ""
        return url


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,help_text="name",null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_order = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.id)
    
  

class OrderItem(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    qty = models.IntegerField(default=0,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} "
    
    @property
    def get_total(self):
        total = self.product.price * self.qty
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems= self.orderitem_set.all()
        total= sum([item.qty for item in orderitems])
        return total

    
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    product = models.ForeignKey(Products,on_delete=models.SET_NULL,blank=True,null=True) 
    phone_no = models.PositiveIntegerField(help_text="07********")
    county = models.CharField(max_length=30,help_text="your county")
    town = models.CharField(max_length=50,help_text="nearest shopping centre or town")
    pick_point = models.CharField(max_length=70,help_text="exact point of colleection")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pick_point}"










    


