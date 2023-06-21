from django.contrib import admin
from django.urls import path,include
from cart.views import AddToCart,cart_remove
from cart import views
app_name ='cart'
urlpatterns = [
    path('addcart/<int:s>/', views.AddToCart, name="addcart"),
    path('cart_view/',views.cart_view,name='cart_view'),
    path('cart_remov/<int:p>/',views.cart_remove,name='cartremove'),
    path('fullremove/<int:p>/',views.fullremove,name='fullremove'),
    path('accountorder/',views.accountorder,name='accountorder'),
    path('orderdetail/',views.orderdetail,name='orderdetail'),
    path('yourorder/',views.yourorder ,name='yourorder'),
]