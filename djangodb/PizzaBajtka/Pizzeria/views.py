from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    return render(request, 'home.html', {})


def warehouse(request):
    return render(request, 'warehouse.html', {'all': Product.objects.all})


def orders(request):
    return render(request, 'orders.html', {'all': PizzaOrder.objects.all})

def error(request):
    return render(request, 'error.html', {})


def make_delivery(request):
    form = EditProductForm()
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['Ilosc'] <= 0.0:
                return redirect('error')
            p = Product.objects.get(name = cd['Produkt'])
            p.volume += cd['Ilosc']
            p.save()
            return redirect('/')
        else:
            return redirect('/')
    return render(request, 'make_delivery.html', {'form': form})

def make_product(request):
    form = NewProductForm()
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            p = Product()
            p.name = cd['Produkt']
            p.volume = 0.0
            x = Product.objects.filter(name = p.name).count()
            if(x > 0):
                return redirect('error')
            p.save()
            return redirect('/')
        else:
            return redirect('/')
    return render(request, 'make_product.html', {'form': form})

def make_order(request, order = None, flag = True):
    form = OrderForm()
    if request.method == 'POST' and flag:
        order = Order.objects.all().last()
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['Ilosc'] <= 0.0:
                return redirect('error')
            po = PizzaOrder()
            po.pizza=cd['Pizza']
            po.order=order
            po.size=cd['Size']
            po.amount=cd['Ilosc']
            print(po.size.ingredientMultiplier)
            for i in Ingredient.objects.filter(pizza=po.pizza):
                if i.amount * po.amount * po.size.ingredientMultiplier > i.product.volume:
                    return redirect('error')

            for i in Ingredient.objects.filter(pizza=po.pizza):
                i.product.volume -= i.amount * po.amount * po.size.ingredientMultiplier
                i.product.save()
            
            po.save()   
        return make_order(request, order, False)
    if order is None:
        order = Order()
        order.save()
    return render(request, 'make_order.html', {'order': order, 'form': form, 'all': PizzaOrder.objects.filter(order=order)})

def make_pizza(request):
    form = NewPizzaForm()
    if request.method == 'POST':
        form = NewPizzaForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            p = Pizza()
            p.name = cd['Pizza']
            x = Pizza.objects.filter(name = p.name).count()
            if(x > 0):
                return redirect('error')
            p.price = cd['Cena']
            if(p.price <= 0.0):
                return redirect('error')
            p.save()
            return redirect('add_indigrient_to_pizza')
        else:
            return redirect('/')
    return render(request, 'make_pizza.html', {'form': form})

def add_indigrient_to_pizza(request):
    form = EditProductForm()
    pizza = Pizza.objects.all().last()
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            ing = Ingredient()
            ing.pizza = pizza
            ing.product = cd['Produkt']
            x = Ingredient.objects.filter(pizza=pizza, product=ing.product).count()
            if(x > 0):
                return redirect('error')
            ing.amount = cd['Ilosc']
            if ing.amount <= 0.0:
                return redirect('error')
            ing.save()
            return redirect('add_indigrient_to_pizza')
        else:
            return redirect('/')
    return render(request, 'add_indigrient_to_pizza.html', {'pizza': pizza, 'form': form, 'all': Ingredient.objects.filter(pizza=pizza)})

def menu(request):
    return render(request, 'menu.html', {'all': Ingredient.objects.all, 'sizes': PizzaSize.objects.all,})