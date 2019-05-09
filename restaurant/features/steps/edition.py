from behave import *
from behave import when

use_step_matcher("parse")


@when('I edit the client with nif "{nif}"')
def step_impl(context, nif):
    from clients.models import Client
    client = Client.objects.get(name=nif)
    context.browser.visit(context.get_url('clients:client_edit', client.pk))
    if context.browser.url == context.get_url('clients:client_edit', client.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()


@when('I edit the table with table_num "{table_number}"')
def step_impl(context, table_number):
    from clients.models import Table
    table = Table.objects.get(tab=table_number)
    context.browser.visit(context.get_url('clients:table_edit', table.pk))
    if context.browser.url == context.get_url('clients:table_edit', table.pk) \
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()

@when('I edit the order with orderid "{orderid}"')
def step_impl(context, orderid):
    from clients.models import Order
    order = Order.objects.get(id=orderid)
    context.browser.visit(context.get_url('clients:order_edit', order.pk))
    if context.browser.url == context.get_url('clients:order_edit', order.pk) \
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()

@when('I edit the waiter with waiterid "{waiterid}"')
def step_impl(context, waiterid):
    from clients.models import Waiter
    waiter = Waiter.objects.get(wait=waiterid)
    context.browser.visit(context.get_url('clients:waiter_edit', waiter.pk))
    if context.browser.url == context.get_url('clients:waiter_edit', waiter.pk) \
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()


@when('I edit the dish with meal_id "{meal_id}"')
def step_impl(context, meal_id):
    from clients.models import Dishes
    dishes = Dishes.objects.get(meal=meal_id)
    context.browser.visit(context.get_url('clients:dishes_edit', dishes.pk))
    if context.browser.url == context.get_url('clients:dishes_edit', dishes.pk) \
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()
