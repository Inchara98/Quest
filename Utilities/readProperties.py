import configparser
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import webdriver, options

config = configparser.RawConfigParser()
config.read("/home/inchara/PycharmProjects/Quest/Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def get_chrome_driver_directory():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("Utilities", "")
        chrome_directory_path = os.path.join(current_directory, '/home/inchara/PycharmProjects/Quest/driver'
                                                                '/chromedriver')
        return chrome_directory_path

    @staticmethod
    def get_firefox_driver_directory():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("Utilities", "")
        firefox_directory_path = os.path.join(current_directory, '/home/inchara/PycharmProjects/Quest/driver'
                                                                 '/geckodriver')
        return firefox_directory_path

    @staticmethod
    def get_application_url():
        url = config.get('common_info', 'baseUrl')
        return url

    @staticmethod
    def getUserID():
        username = config.get('common_info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password

    @staticmethod
    def getUser():
        Fakeusername = config.get('common_info', 'FakeUsername')
        return Fakeusername

    @staticmethod
    def getpassword():
        FakePassword = config.get('common_info', 'FakePassword')
        return FakePassword

    @staticmethod
    def getEmpty():
        Empty = config.get('common_info', 'Empty')
        return Empty

    @staticmethod
    def getApplicationUrl1():
        url = config.get('common_info', 'baseUrl(AT)')
        return url

    @staticmethod
    def getUserID1():
        username = config.get('common_info', 'username(AT)')
        return username

    @staticmethod
    def getPassword1():
        password = config.get('common_info', 'password(AT)')
        return password

    @staticmethod
    def get_download_dir():
        cwd = os.path.dirname(__file__)
        download_path = os.path.join(cwd, 'Downloads')
        return download_path

    @staticmethod
    def get_ss_path():
        cwd = os.path.dirname(__file__)
        ss_path = os.path.join(cwd, '../Screenshots/')
        return ss_path

    @staticmethod
    def get_logs_directory():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("Utilities", "")
        logs_directory = os.path.join(current_directory, 'Logs')
        return logs_directory
