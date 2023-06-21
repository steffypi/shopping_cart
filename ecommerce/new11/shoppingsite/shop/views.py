from django.shortcuts import render
from shop.models import Category,Product
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def allProdCat(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def productview(request,cslug):
    c=Category.objects.get(slug=cslug)
    p=Product.objects.filter(category__slug=cslug)
    return render(request,'productview.html',{'p':p,'c':c})

def productsdetail(request,dslug):
    d=Product.objects.get(slug=dslug)
    return render(request,'productdetail.html',{'d':d})



def register(request):
    if(request.method=="POST"):
        ak = request.POST['ak']
        ab = request.POST['ab']
        ac = request.POST['ac']
        ad = request.POST['ad']
        ae = request.POST['ae']
        af = request.POST['af']
        if ae==af:
            user= User.objects.create_user(username=ak,first_name=ab,last_name=ac,email=ad,password=ae)
            user.save()
            return allProdCat(request)
    return render(request,"register.html")


def login_user(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return allProdCat(request)
        else:
            messages.error(request,"inalid credentials")
    return render(request,"login.html")


def logout_user(request):
    logout(request)
    return allProdCat(request)
    
def AddToCart(request):
    return render(request,"addToCart.html")
    