from django.shortcuts import render, redirect

from .models import *

def home(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'all' not in request.session:
        request.session['all'] = 0

    all_items = {
        "items": Item.objects.all()
    }
    return render(request, "home.html", all_items)

def buy(request):
    if request.method == 'POST':
        item = Item.objects.get(id = int(request.POST['product_id']))
        total_price = item.price * int(request.POST['quantity'])
        request.session['total_price'] = total_price
        request.session['count'] = request.session['count'] + int(request.POST['quantity'])
        request.session['all'] = request.session['all'] + total_price
        return redirect('/amadon/checkout')
    else:
        return redirect('/amadon')

def checkout(request):
    return render(request, "checkout.html")

def clear(request):
    request.session.clear()
    return redirect('/amadon')