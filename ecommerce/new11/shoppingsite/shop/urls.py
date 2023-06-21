from django.contrib import admin
from django.urls import path,include
from shop.views import *
from shop import views

app_name = 'shop'
urlpatterns = [
    path('',views.allProdCat,name="category"),
    path('productview/<slug:cslug>/', views.productview, name="productview"),
    path('productdetail/<slug:dslug>/', views.productsdetail, name="product"),
    path('register/', views.register, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/',views.logout_user, name="logout"),
   
]
