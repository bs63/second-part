from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ClientForm, TableForm, OrderForm, WaiterForm, DishesForm, MenuForm, ReviewForm
from .models import Client, Table, Order, Waiter, Dishes, Menu, Review
from django.views.generic.detail import DetailView


def home(request):
    return render(request, 'clients/index.html')


def client_list(request, template_name='clients/client_list.html'):
    client = Client.objects.all()
    data = {}
    data['object_list'] = client
    return render(request, template_name, data)

def client_view(request, pk, template_name='clients/client_detail.html'):
    client= get_object_or_404(Client, pk=pk)
    return render(request, template_name, {'object':client})

def ClientCreate(request, template_name= 'clients/login.html'):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    return render(request, 'clients/form.html', {'form': form})


def client_update(request, pk):
    client = get_object_or_404(Client, id=pk)
    form = ClientForm(request.POST or None, instance= client)

    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'clients/form.html', {'form': form})


def client_delete(request, pk, template_name= 'clients/client_confirm_delete.html'):
    client= get_object_or_404(Client, id=pk)
    if request.method=='POST':
        client.delete()
        return redirect('client_list')
    return render(request, template_name, {'object':client})

def backbutton(request):
    return redirect('index')


def table_list(request, template_name='clients/table_list.html'):
    table = Table.objects.all()
    data = {}
    data['object_list'] = table
    return render(request, template_name, data)

def table_view(request, pk, template_name='clients/table_detail.html'):
    table= get_object_or_404(Table, pk=pk)
    return render(request, template_name, {'object':table})

def TableCreate(request):
    form = TableForm()
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_list')
    return render(request, 'clients/form.html', {'form': form})


def table_update(request, pk):
    table = get_object_or_404(Table, id=pk)
    form = TableForm(request.POST or None, instance= table)

    if form.is_valid():
        form.save()
        return redirect('table_list')
    return render(request, 'clients/form.html', {'form': form})


def table_delete(request, pk, template_name= 'clients/table_confirm_delete.html'):
    table= get_object_or_404(Table, id=pk)
    if request.method=='POST':
        table.delete()
        return redirect('table_list')
    return render(request, template_name, {'object':table})


def order_list(request, template_name='clients/order_list.html'):
    order = Order.objects.all()
    data = {}
    data['object_list'] = order
    return render(request, template_name, data)

def order_view(request, pk, template_name='clients/order_detail.html'):
    order= get_object_or_404(Order, pk=pk)
    return render(request, template_name, {'object':order})

def OrderCreate(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    return render(request, 'clients/form.html', {'form': form})


def order_update(request, pk):
    order = get_object_or_404(Order, id=pk)
    form = OrderForm(request.POST or None, instance= order)

    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'clients/form.html', {'form': form})


def order_delete(request, pk, template_name= 'clients/order_confirm_delete.html'):
    order= get_object_or_404(Order, id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('order_list')
    return render(request, template_name, {'object':order})


def waiter_list(request, template_name='clients/waiter_list.html'):
    waiter = Waiter.objects.all()
    data = {}
    data['object_list'] = waiter
    return render(request, template_name, data)

def waiter_view(request, pk, template_name='clients/waiter_detail.html'):
    waiter= get_object_or_404(Waiter, pk=pk)
    return render(request, template_name, {'object':waiter})

def WaiterCreate(request):
    form = WaiterForm()
    if request.method == "POST":
        form = WaiterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('waiter_list')
    return render(request, 'clients/form.html', {'form': form})


def waiter_update(request, pk):
    waiter = get_object_or_404(Waiter, id=pk)
    form = WaiterForm(request.POST or None, instance= waiter)

    if form.is_valid():
        form.save()
        return redirect('waiter_list')
    return render(request, 'clients/form.html', {'form': form})


def waiter_delete(request, pk, template_name= 'clients/waiter_confirm_delete.html'):
    waiter= get_object_or_404(Waiter, id=pk)
    if request.method=='POST':
        waiter.delete()
        return redirect('waiter_list')
    return render(request, template_name, {'object':waiter})

def dishes_list(request, template_name='clients/dishes_list.html'):
    dishes = Dishes.objects.all()
    data = {}
    data['object_list'] = dishes
    return render(request, template_name, data)

def dishes_view(request, pk, template_name='clients/dishes_detail.html'):
    dishes= get_object_or_404(Dishes, pk=pk)
    return render(request, template_name, {'object':dishes})

def DishesCreate(request):
    form = DishesForm()
    if request.method == "POST":
        form = DishesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dishes_list')
    return render(request, 'clients/form.html', {'form': form})


def dishes_update(request, pk):
    dishes = get_object_or_404(Dishes, id=pk)
    form = DishesForm(request.POST or None, instance= dishes)

    if form.is_valid():
        form.save()
        return redirect('dishes_list')
    return render(request, 'clients/form.html', {'form': form})


def dishes_delete(request, pk, template_name= 'clients/dishes_confirm_delete.html'):
    dishes= get_object_or_404(Dishes, id=pk)
    if request.method=='POST':
        dishes.delete()
        return redirect('dishes_list')
    return render(request, template_name, {'object':dishes})



def menu_list(request, template_name='clients/menu_list.html'):
    menu = Menu.objects.all()
    data = {}
    data['object_list'] = menu
    return render(request, template_name, data)

def menu_view(request, pk, template_name='clients/menu_detail.html'):
    menu= get_object_or_404(Menu, pk=pk)
    return render(request, template_name, {'object':menu})

def MenuCreate(request):
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    return render(request, 'clients/form.html', {'form': form})


def menu_update(request, pk):
    menu = get_object_or_404(Menu, id=pk)
    form = MenuForm(request.POST or None, instance= menu)

    if form.is_valid():
        form.save()
        return redirect('menu_list')
    return render(request, 'clients/form.html', {'form': form})


def menu_delete(request, pk, template_name= 'clients/menu_confirm_delete.html'):
    menu= get_object_or_404(Menu, id=pk)
    if request.method=='POST':
        menu.delete()
        return redirect('menu_list')
    return render(request, template_name, {'object':menu})


def review_list(request, template_name='clients/review_list.html'):
    review = Review.objects.all()
    data = {}
    data['object_list'] = review
    return render(request, template_name, data)

def review_view(request, pk, template_name='clients/review_detail.html'):
    review= get_object_or_404(Review, pk=pk)
    return render(request, template_name, {'object':review})

def ReviewCreate(request):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    return render(request, 'clients/form.html', {'form': form})


def review_update(request, pk):
    review = get_object_or_404(Review, id=pk)
    form = ReviewForm(request.POST or None, instance= review)

    if form.is_valid():
        form.save()
        return redirect('review_list')
    return render(request, 'clients/form.html', {'form': form})


def review_delete(request, pk, template_name= 'clients/review_confirm_delete.html'):
    review= get_object_or_404(Review, id=pk)
    if request.method=='POST':
        review.delete()
        return redirect('review_list')
    return render(request, template_name, {'object':review})
