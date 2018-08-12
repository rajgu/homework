

class BasePage(object):


    def __init__(self, context):
        self.browser = context.browser
        self.timeout = context.options['timeout']


    def open(self, url):
        self.browser.get(url)


    def __getattr__(self, attr):
        if attr in self.locators:
            return self.browser.find_element(*self.locators[attr])
        else:
            raise Exception("Locator: '{0}' does not exists".format(attr))
