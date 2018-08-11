from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class FSecureCareerPage(BasePage):


	def __init__(self, context):
		BasePage.__init__(self, context)


	locators = {
		'open_jobs_button':  (By.XPATH, '//*[@id="p_p_id_56_INSTANCE_gJitE6b6gf8s_"]/div/div/div/div[1]/section/div/div[2]/div[2]/div/a')
	}

