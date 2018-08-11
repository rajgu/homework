from behave import given, when, then
from pages.BasePage import BasePage
from pages.FSecureHomePage import FSecureHomePage


@given("open F-Secure web page")
def open_fsecure_web_page(context):
    page = BasePage(context)
    page.open("https://www.f-secure.com/en/welcome")
    context.windows = [context.browser.window_handles[0]]


@then("I accept cookies statement")
def accept_cookies(context):
	page = FSecureHomePage(context)
	page.cookie_consent.click()


@then("I click on career button")
def click_on_career_button(context):
	page = FSecureHomePage(context)
	page.career_button.click()
