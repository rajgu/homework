from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.BasePage import BasePage


class FSecureJobOfferPage(BasePage):


	def __init__(self, context):
		BasePage.__init__(self, context)
		WebDriverWait(self.browser, self.timeout).until(expected_conditions.visibility_of_element_located(self.locators['page_main_object']))


	def getRequirements(self):
		req_list_object = self.requirements_list
		req_list = list(map(lambda x: x.text, req_list_object.find_elements_by_tag_name('li')))
		return req_list


	def getCoworkers(self):
		coworkers_list = list(map(lambda x: x.text, self.browser.find_elements(*self.locators['coworker_name_div'])))
		return coworkers_list


	locators = {
		'page_main_object':  (By.XPATH, '//div[contains(@class, "canvas-job-description")]'),
		'requirements_list': (By.XPATH, '//*[@id="canvas-ad-container"]/div[4]/div/div/div/ul'),
		'coworker_name_div': (By.XPATH, '//div[contains(@class, "name")]')
	}
