from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class FSecureHomePage(BasePage):


	def __init__(self, context):
		BasePage.__init__(self, context)


	locators = {
		'cookie_consent': (By.XPATH, '//*[@id="cookie-consent"]/span/a[2]'),
		'career_button':  (By.XPATH, '//*[@id="about"]/li[4]/a')
	}

