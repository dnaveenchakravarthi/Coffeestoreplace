from django.shortcuts import render,redirect,get_list_or_404
from django.http import HttpResponse
from .models import Coffee
# Create your views here.
def home(request):
    coffee=Coffee.objects.all()
    return render(request,'coffee/home.html',context={'coffee':coffee})

def add_to_cart(request,coffee_id):
    cart=request.session.get('cart',{})
    cart[coffee_id]=cart.get(coffee_id,0)+1
    request.session['cart']=cart
    return redirect('cart_view')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for coffee_id, quantity in cart.items():
        coffee = Coffee.objects.get(id=coffee_id)
        item_total = coffee.price * quantity
        total_price += item_total
        cart_items.append({
            'coffee': coffee,
            'quantity': quantity,
            'item_total': item_total
        })

    return render(request, 'coffee/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def remove_from_cart(request, coffee_id):
    cart = request.session.get('cart', {})
    coffee_id = str(coffee_id)

    if coffee_id in cart:
        del cart[coffee_id]
        request.session['cart'] = cart

    return redirect('cart_view')