from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.BasePage import BasePage
from lib.JobOfferArticle import JobOfferArticle


class FSecureJobOpeningsListPage(BasePage):


	def __init__(self, context):
		BasePage.__init__(self, context)
		WebDriverWait(self.browser, self.timeout).until(expected_conditions.visibility_of_element_located(self.locators['cities_list_select']))


	def selectCity(self, city):
		Select(self.cities_list_select).select_by_value(city)
		WebDriverWait(self.browser, self.timeout).until(expected_conditions.visibility_of_element_located(self.locators['first_job_article']))


	def getJobOffer(self, jobName):
		jobsList = self.jobs_list_div.find_elements_by_tag_name('article')
		for job in jobsList:
			JobOffer = JobOfferArticle(job)
			if JobOffer.getJobName() == jobName:
				return JobOffer

		raise Exception("Could not find Job: '{0}'".format(jobName))


	locators = {
		'cities_list_select': (By.ID, 'job-city'),
		'first_job_article':  (By.XPATH, '//*[@id="job-ads"]/article[1]'),
		'jobs_list_div':      (By.ID, 'job-ads')
	}
