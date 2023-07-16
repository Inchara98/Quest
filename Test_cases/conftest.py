from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from Utilities.readProperties import ReadConfig


@pytest.fixture()
def setup(browser):
    chromeOptions = Options()
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': ReadConfig.get_download_dir()}
    options.add_experimental_option('prefs', prefs)
    options.add_argument("--window-size=3860,2160")
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    chromeOptions.add_experimental_option("prefs",
                                          {"download.default_directory": "/home/inchara/PycharmProjects/Quest/Downloads"})
    service = Service(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    if browser == 'chrome':
        service = Service(executable_path="/home/inchara/PycharmProjects/Quest/driver/chromedriver",
                                  chrome_options=chromeOptions)
        driver = webdriver.Chrome(service=service)
        print("Launching chrome browser.......")
    elif browser == 'firefox':
        service = Service(executable_path="/home/inchara/PycharmProjects/Quest/driver/geckodriver")
        driver = webdriver.Firefox(service=service)
        print("Launching firefox browser.......")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report #############
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Quest'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Inchara'

#
# # It is hooked for delete/modify Environment info to Html Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
