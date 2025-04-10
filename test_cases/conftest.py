import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
import undetected_chromedriver as uc  #add this import to bypass captcha

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        #Use undetected_chromedriver here
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = uc.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported Browser")

    driver.maximize_window()
    return driver

# HTML report metadata
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project, Test automation'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'Roshan Nepal'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Packages', None)
    metadata.pop('Plugins', None)
#The old code was not able to handle captcha, so we use undetected chromedriver to bypass that
#This is the old code
# from email.policy import default
#
# import pytest
# from selenium import webdriver
# from pytest_metadata.plugin import metadata_key #to generate HTML reports
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action = "store", default = "chrome",
#                     help = "Specify the browser: chrome or firefox or edge")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture()
# def setup(browser):
#     global driver
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver =webdriver.Firefox()
#     elif browser == "edge":
#         driver = webdriver.Edge()
#     else:
#         raise ValueError("Unsupported Browser")
#
#     return driver
#
# #To execute test in different browser: pytest -s -v .\test_cases\test_admin_login.py --browser edge or firefox or chrome
# #To execute tests in parallel: pytest -v -s .\test_cases\test_admin_login.py -n 3, where n = number of workers
# #To generate HTML reports: pytest -v -s --html reports/report.html
#
#
# ##For PyTest HTML reports##
# #Hook for adding custom environment info into HTML reports
# def pytest_configure(config):
#     config.stash[metadata_key] ['Project Name'] = 'Ecommerce Project, Test automation'
#     config.stash[metadata_key] ['Test Module Name'] = 'Admin Login Tests'
#     config.stash[metadata_key] ['Tester Name'] = 'Roshan Nepal'
#
# #Hoook for deleting/modifying environment into HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('Packages', None)
#     metadata.pop('Plugins', None)

#This is the older Code, no mechanism to run tests on multiple browsers and generate HTML reports
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver

#The old code was not able to handle captcha, so we use undetected chromedriver to bypass that

