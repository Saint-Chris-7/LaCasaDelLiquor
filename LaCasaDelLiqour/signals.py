from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Customer
from django.dispatch import receiver

@receiver(post_save,sender=User)
def customer_save_signal(sender,instance,created,**kwargs):
    if created:
        Customer.objects.create(user=instance)


