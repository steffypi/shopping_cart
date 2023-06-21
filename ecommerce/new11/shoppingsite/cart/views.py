from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from shop.models import Category,Product
from cart.models import Cart,Order,Account



@login_required
def cart_view(request):
    total=0
    try:
        user=request.user
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total+=i.quantity*i.products.price
    except Cart.DoesNotExist:
        pass
    return render(request,'AddToCart.html',{'cart':cart,'total':total})

@login_required
def AddToCart(request,s):
    products=Product.objects.get(id=s)
    user=request.user
    try:
        cart=Cart.objects.get(products=products,user=user)
        if cart.quantity<cart.products.stock:
            cart.quantity+=1
        cart.save()
    except:
        cart=Cart.objects.create(products=products,user=user,quantity=1)
        cart.save()
    return redirect("cart:cart_view")

@login_required
def cart_remove(request,p):
    products=Product.objects.get(id=p)
    user = request.user
    try:
        cart=Cart.objects.get(user=user,products=products)
        if cart.quantity>1:
            cart.quantity-=1
            cart.save()
        else:
            cart.delete()
    except:
         pass
    return redirect('cart:cart_view')
            
@login_required        
def fullremove(request,p):
    products = Product.objects.get(id=p)
    user = request.user
    try:
        cart = Cart.objects.get(user=user, products=products)
        cart.delete()
    except:
        pass
    return redirect('cart:cart_view')



def orderdetail(request):
    return render(request,'orderdetail.html')


@login_required
def accountorder(request):
    total=0
    if (request.method == "POST"):
        t = request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        user=request.user
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total+=i.quantity*i.products.price
            a=Account.objects.get(accountnumber=p)
        if float(a.amount) >=total:
            a.amount=a.amount-total
            a.save()
            for i in cart:
                o=Order(user=user,product=i.products,adress=a,phone=p,order_status="paid",noofitems=i.quantity)
                o.save()
            cart.delete()
            msg="order places successfully"
            return render(request,'orderdetail.html',{'msg':msg,'total':total})

        else:
            msg="insufficient Amount,you cant place order"
            return render(request,'orderdetail.html',{"msg":msg})
            pass
    return render(request,"account.html")

@login_required
def yourorder(request):
    user=request.user
    o=Order.objects.filter(user=user,order_status="paid")
    return render(request,'yourorder.html',{'o':o,'name':user.username})