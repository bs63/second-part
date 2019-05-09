from django import forms
from .models import Client, Table, Order, Waiter, Dishes, Menu, Review



class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('nif', 'Fname', 'Lname', 'address', 'phone_number',)

class TableForm(forms.ModelForm):

    class Meta:
        model = Table
        fields = ('table_number', 'capacity', 'status', 'num_per_sitting', 'serv_staff_id', 'client', )

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('orderid', 'order_date', 'client', 'quantity', 'pick_up_date', )

class WaiterForm(forms.ModelForm):

    class Meta:
        model = Waiter
        fields = ('waiterid', 'lastname', 'firstname', 'Username', 'phone_number_wait', 'password', 'order', )

class DishesForm(forms.ModelForm):

    class Meta:
        model = Dishes
        fields = ('meal_id', 'name', 'date_of_meal', 'price', 'description', 'rating', 'images', 'similardishes', )

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('dish', )

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'comment', 'date', 'client', )
