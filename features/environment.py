from selenium import webdriver
import os


def before_all(context):
    context.options = {}
    if 'browser' in context.config.userdata and context.config.userdata['browser'] is not None:
        context.options['browser'] = context.config.userdata['browser']
    else:
        context.options['browser'] = 'chrome'

    if 'timeout' in context.config.userdata and context.config.userdata['timeout'].isnumeric():
        context.options['timeout'] = int(context.config.userdata['timeout'])
    else:
        context.options['timeout'] = 10


def before_scenario(context, scenario):
    if context.options['browser'] == 'firefox':
        drivers_directory = os.path.dirname(os.path.abspath(__file__)) + "/../drivers"
        os.environ["PATH"] += os.pathsep + drivers_directory
        context.browser = webdriver.Firefox()
    elif context.options['browser'] == 'chrome':
        context.browser = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__)) + "/../drivers/chromedriver")
    else:
        raise Exception("Try to use unsupported browser: {0}".format(context.config.userdata['browser']))

    context.browser.maximize_window()


def after_scenario(context, scenario):
    print("Scenario Ended, status: {0}".format(scenario.status))
    context.browser.quit()
