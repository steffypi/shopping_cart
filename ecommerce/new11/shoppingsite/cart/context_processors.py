from cart.models import Cart
# 
# 
def counter(request):
    pass
    item_count=0
    if request.user.is_authenticated:
        user=request.user
    try:
        carts=Cart.objects.filter(user=user)
        for i in carts:
         item_count+=i.quantity
    except Cart.DoesNotExist:
        item_count=0
    return {'item_count':item_count}