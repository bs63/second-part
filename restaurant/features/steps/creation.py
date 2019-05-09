from behave import *

use_step_matcher("re")


@when('I register a Client')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('clients:client_list'))
        context.browser.visit(context.get_url('clients:client_new'))
        if context.browser.url == context.get_url('clients:client_new'):
            if not context.browser.is_text_present("403"):
                form = context.browser.find_by_tag('form').first
                for heading in row.headings:
                    context.browser.fill(heading, row[heading])
                form.find_by_value('Submit').first.click()


@when('I register a Table')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('clients:table_list'))
        context.browser.visit(context.get_url('clients:table_new'))
        if context.browser.url == context.get_url('clients:table_new'):
            if not context.browser.is_text_present("403"):
                form = context.browser.find_by_tag('form').first
                for heading in row.headings:
                    context.browser.fill(heading, row[heading])
                form.find_by_value('Submit').first.click()


@when('I register an Order')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('clients:order_list'))
        context.browser.visit(context.get_url('clients:order_new'))
        if context.browser.url == context.get_url('clients:order_new'):
            if not context.browser.is_text_present("403"):
                form = context.browser.find_by_tag('form').first
                for heading in row.headings:
                    context.browser.fill(heading, row[heading])
                form.find_by_value('Submit').first.click()


@when('I register a Waiter')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('clients:waiter_list'))
        context.browser.visit(context.get_url('clients:waiter_new'))
        if context.browser.url == context.get_url('clients:waiter_new'):
            if not context.browser.is_text_present("403"):
                form = context.browser.find_by_tag('form').first
                for heading in row.headings:
                    context.browser.fill(heading, row[heading])
                form.find_by_value('Submit').first.click()


@when('I register a Dishes')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('clients:dishes_list'))
        context.browser.visit(context.get_url('clients:dishes_new'))
        if context.browser.url == context.get_url('clients:dishes_new'):
            if not context.browser.is_text_present("403"):
                form = context.browser.find_by_tag('form').first
                for heading in row.headings:
                    context.browser.fill(heading, row[heading])
                form.find_by_value('Submit').first.click()



@when('I register a Menu')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('clients:menu_list'))
        context.browser.visit(context.get_url('clients:menu_new'))
        if context.browser.url == context.get_url('clients:menu_new'):
            if not context.browser.is_text_present("403"):
                form = context.browser.find_by_tag('form').first
                for heading in row.headings:
                    context.browser.fill(heading, row[heading])
                form.find_by_value('Submit').first.click()

@when('I register a Review')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('clients: review_list'))
        context.browser.visit(context.get_url('clients: review_new'))
        if context.browser.url == context.get_url('clients:review_new'):
            if not context.browser.is_text_present("403"):
                form = context.browser.find_by_tag('form').first
                for heading in row.headings:
                    context.browser.fill(heading, row[heading])
                form.find_by_value('Submit').first.click()
