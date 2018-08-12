

class JobOfferArticle(object):


    def __init__(self, jobWebElement):
        self.jobWebElement = jobWebElement
        self.jobName = self.jobWebElement.find_element_by_tag_name('h2').text
        self.jobCity = self.jobWebElement.find_element_by_tag_name('p').text
        self.jobLink = self.jobWebElement.find_element_by_tag_name('a')


    def getJobName(self):
        return self.jobName


    def setJobNameName(self, jobName):
        self.jobName = jobName


    def getjobCity(self):
        return self.jobCity


    def setJobCity(self, jobCity):
        self.jobCity = jobCity


    def getJobLink(self):
        return self.jobLink
