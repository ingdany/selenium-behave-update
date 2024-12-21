from behave import *

from features.pages.dashboard_page import DashboardPage
from features.pages.login_page import LoginPage

@given(u'I open orange HRM Homepage')
def step_impl(context):
    page = LoginPage(context)
    page.visit("https://opensource-demo.orangehrmlive.com/")

@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    page = LoginPage(context)
    page.type_user(user)
    page.type_password(pwd)

@when(u'Click in login button')
def step_impl(context):
    page = LoginPage(context)
    page.click_button()


@then(u'User must validate if display "{text}" in the Dashboard page')
def step_impl(context, text):
    try:
        page = DashboardPage(context)
        page.verify_label(text)
    except:
        context.browser.close()
    