from behave import given, when, then
from pages.FSecureCareerPage import FSecureCareerPage
from pages.FSecureJobOpeningsListPage import FSecureJobOpeningsListPage
from pages.FSecureJobOfferPage import FSecureJobOfferPage
import time

use_step_matcher("re")


@then("I click on open jobs button")
def click_on_open_jobs_button(context):
	page = FSecureCareerPage(context)
	page.open_jobs_button.click()


@then("From available cities I select '([^']*)'")
def select_city_from_list(context, city):
	page = FSecureJobOpeningsListPage(context)
	page.selectCity(city)


@then("I click on '([^']*)' offer")
def click_on_specific_job_offer(context, jobName):
	page = FSecureJobOpeningsListPage(context)
	num_pages = len(context.browser.window_handles)
	page.getJobOffer(jobName).getJobLink().click()
	time_start = time.time()
	while num_pages == len(context.browser.window_handles):
		time.sleep(0.1)
		if time.time() - context.options['timeout'] > time_start:
			raise Exception("New window did not open within declared timeout: {0}s".format(context.options['timeout'])) 

	context.windows.append(context.browser.window_handles[num_pages])
	context.browser.switch_to_window(context.browser.window_handles[num_pages]);


@when("I check if '([^']*)' is on requirements list")
def check_offer_requirements_list(context, requirement):
	page = FSecureJobOfferPage(context)
	assert(requirement in page.getRequirements())


@when("I verify that i will be working with '([^']*)'")
def check_offer_for_coworker(context, name):
	page = FSecureJobOfferPage(context)
	assert(name in page.getCoworkers())
