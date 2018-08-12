from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.BasePage import BasePage


class FSecureHomePage(BasePage):


    def __init__(self, context):
        BasePage.__init__(self, context)
        WebDriverWait(self.browser, self.timeout).until(expected_conditions.visibility_of_element_located(self.locators['page_main_object']))


    locators = {
        'page_main_object': (By.ID,    'gn'),
        'cookie_consent':   (By.XPATH, '//*[@id="cookie-consent"]/span/a[2]'),
        'career_button':    (By.XPATH, '//*[@id="about"]/li[4]/a')
    }

