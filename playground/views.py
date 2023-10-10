from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Item
from .forms import *


def say_hello(request):
    return render(request, "hello.html")



def signuppage(request):
    return render(request, "signuppage.html")
    pass

def home(request):
    return render(request, "home.html")
    pass


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        amount = request.POST.get('amount')
        user = User(name=username,password=password,currency_amount=amount) 
        user.save()
        return HttpResponse(f'UserSuccessfully Saved <br> Username: {username}, Password: {password}, InitalAmount: {amount}')
      
    pass

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        u = User.objects.filter(name=username, password=password)
        if u is not None:
            return render(request, "home.html") 
        else:
            return HttpResponse(f'Failed Logging')

def user_loginpage(request):
    return render(request, "loginpage.html")
    pass


def buy(request):
    items = Item.objects.filter(is_selling=True)
    return render(request, 'item_list.html', {'items': items})


def buy_item(request, item_name):
    try:
        item = Item.objects.get(name=item_name)
    except Item.DoesNotExist:
        return HttpResponse(f'Error') 

    if request.method == 'POST':
        form = BuyItemForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            return redirect('bought', item_name=item_name, username=username, password=password)
    else:
        form = BuyItemForm()

    return render(request, 'buyitem.html', {'item': item, 'form': form})


def bought(request, item_name, username, password):
    try:
        u = User.objects.filter(name=username, password =password).get()   
    except: 
        return HttpResponse(f'Error') 

    if u is not None:
        i = Item.objects.get(name=item_name)
        if i.owner == u:
            return HttpResponse(f'Error') 
        i.owner = u
        if u.currency_amount >= i.price:
            beforetransaction = u.currency_amount
            u.currency_amount -= i.price
            i.is_selling = False
            i.save()
            u.save()
        else:
            return HttpResponse(f'Amt insufficient') 
        aftertransaction = u.currency_amount
        return HttpResponse(f'Successfully Bought {item_name} by {u.name}<br> Amt BeforeTransaction: {beforetransaction} <br> Amt afterTransaction: {aftertransaction}') 


def sell(request):
    return render(request, 'sell.html')

def sellitem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        owner = request.POST.get('owner')
        password = request.POST.get('password')

        try:
            u = User.objects.filter(name=owner, password = password).get() 
            i = Item(name=name, price=price, owner=u, is_selling=True) 
            i.save()
        except:
            return HttpResponse(f'Error {x}') 
        return HttpResponse(f'Successfully Advertised')
     

