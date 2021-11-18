from django.db import models
from django.db.models.base import Model
from django.forms import ModelForm
from .models import ShippingAddress
class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ['customer','product','date_added']