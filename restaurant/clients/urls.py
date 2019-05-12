from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('ss', views.home, name = "index"),
    path('', views.client_list, name='client_list'),
    path('view/<int:pk>', views.client_view, name='client_view'),
    path('client', views.ClientCreate, name= 'client_new'),
    path('back', views.backbutton, name= 'back'),
    path('edit/<int:pk>', views.client_update, name = 'client_edit'),
    path('delete/<int:pk>', views.client_delete, name='client_delete'),

    path('ss', views.home, name = "index"),
    path('tab', views.table_list, name='table_list'),
    path('view/table/<int:pk>', views.table_view, name='table_view'),
    path('table', views.TableCreate, name= 'table_new'),
    path('back', views.backbutton, name= 'back'),
    path('edit/table/<int:pk>', views.table_update, name = 'table_edit'),
    path('delete/table/<int:pk>', views.table_delete, name='table_delete'),

    path('ss', views.home, name = "index"),
    path('ord', views.order_list, name='order_list'),
    path('view/order/<int:pk>', views.order_view, name='order_view'),
    path('order', views.OrderCreate, name= 'order_new'),
    path('back', views.backbutton, name= 'back'),
    path('edit/order/<int:pk>', views.order_update, name = 'order_edit'),
    path('delete/order/<int:pk>', views.order_delete, name='order_delete'),

    path('ss', views.home, name = "index"),
    path('wait', views.waiter_list, name='waiter_list'),
    path('view/waiter/<int:pk>', views.waiter_view, name='waiter_view'),
    path('waiter', views.WaiterCreate, name= 'waiter_new'),
    path('back', views.backbutton, name= 'back'),
    path('edit/waiter/<int:pk>', views.waiter_update, name = 'waiter_edit'),
    path('delete/waiter/<int:pk>', views.waiter_delete, name='waiter_delete'),

    path('ss', views.home, name = "index"),
    path('dish', views.dishes_list, name='dishes_list'),
    path('view/dishes/<int:pk>', views.dishes_view, name='dishes_view'),
    path('dishes', views.DishesCreate, name= 'dishes_new'),
    path('back', views.backbutton, name= 'back'),
    path('edit/dishes/<int:pk>', views.dishes_update, name = 'dishes_edit'),
    path('delete/dishes/<int:pk>', views.dishes_delete, name='dishes_delete'),

    path('ss', views.home, name = "index"),
    path('men', views.menu_list, name='menu_list'),
    path('view/menu/<int:pk>', views.menu_view, name='menu_view'),
    path('menu', views.MenuCreate, name= 'menu_new'),
    path('back', views.backbutton, name= 'back'),
    path('edit/menu/<int:pk>', views.menu_update, name = 'menu_edit'),
    path('delete/menu/<int:pk>', views.menu_delete, name='menu_delete'),

    path('ss', views.home, name = "index"),
    path('rev', views.review_list, name='review_list'),
    path('view/review/<int:pk>', views.review_view, name='review_view'),
    path('review', views.ReviewCreate, name= 'review_new'),
    path('back', views.backbutton, name= 'back'),
    path('edit/review/<int:pk>', views.review_update, name = 'review_edit'),
    path('delete/review/<int:pk>', views.review_delete, name='review_delete'),


]
