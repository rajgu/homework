from selenium import webdriver
import os


def before_scenario(context, scenario):

    if 'BROWSER' in context.config.userdata.keys() and context.config.userdata['BROWSER']:
        browser = context.config.userdata['BROWSER']
    else:
        browser = 'chrome'

    if browser == 'firefox':
        drivers_directory = os.path.dirname(os.path.abspath(__file__)) + "/../drivers"
        os.environ["PATH"] += os.pathsep + drivers_directory
        context.browser = webdriver.Firefox()
    elif browser == 'chrome':
        context.browser = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__)) + "/../drivers/chromedriver")
    else:
        raise Exception("Try to use unsupported browser: {0}".format(context.config.userdata['BROWSER']))

    context.browser.maximize_window()
    context.options = {}
    context.options['timeout'] = 10


def after_scenario(context, scenario):
    print("Scenario Ended, status: {0}".format(scenario.status))
    context.browser.quit()
