from behave import *
from behave import then

use_step_matcher("parse")


@when('I go to the Homepage')
def step_impl(context):
    context.browser.visit(context.get_url('/clients/'))

@when('I view the details for client "{nif}"')
def step_impl(context, nif):
    from clients.models import Client
    client = Client.objects.get(name=nif)
    context.browser.visit(context.get_url('clients:client_view', client.pk))


@when('I view the details for table "{table_number}"')
def step_impl(context, table_number):
    from clients.models import Table
    table = Table.objects.get(tab=table_number)
    context.browser.visit(context.get_url('clients:table_view', table.pk))


@when('I view the details for order "{orderid}"')
def step_impl(context, orderid):
    from clients.models import Order
    order = Order.objects.get(id=orderid)
    context.browser.visit(context.get_url('clients:order_view', order.pk))


@when('I view the details for waiter "{waiterid}"')
def step_impl(context, waiterid):
    from clients.models import Waiter
    waiter = Waiter.objects.get(wait=waiterid)
    context.browser.visit(context.get_url('clients:waiter_view', waiter.pk))


@when('I view the details for dishes "{meal_id}"')
def step_impl(context, meal_id):
    from clients.models import Dishes
    dishes = Dishes.objects.get(meal=meal_id)
    context.browser.visit(context.get_url('clients:dishes_view', dishes.pk))

@when('I view the details for menu "{dish}"')
def step_impl(context, dish):
    from clients.models import Menu
    menu = Menu.objects.get(dish=dish)
    context.browser.visit(context.get_url('clients:menu_view', menu.pk))

@when('I view the details for review "{rati}"')
def step_impl(context, rating):
    from clients.models import Review
    review = Review.objects.get(rat=rating)
    context.browser.visit(context.get_url('clients:# review_view', review.pk))


@then("I'm viewing details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])
