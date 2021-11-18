
from LaCasaDelLiqour import views
from django.urls import path 

urlpatterns  = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('signup/', views.signup, name='signup'),
]