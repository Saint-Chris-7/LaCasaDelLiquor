
from LaCasaDelLiqour import views
from django.urls import path 

urlpatterns  = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]