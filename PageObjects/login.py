import logging
import time

from selenium.webdriver.common.by import By

from Utilities import XLUtils, CustomLogger
from Utilities.readProperties import ReadConfig
from PageObjects.BasePage import Base


class Login(Base):
    username = "username"
    password = "password"
    submit = (By.XPATH, "//button[@type='submit']")
    filename = '/home/inchara/PycharmProjects/Quest/TestData/credentials.csv'
    dropdown = (By.CLASS_NAME, "oxd-userdropdown")
    logout = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]")
    path = "TestData/cred_details1.xlsx"
    logger = CustomLogger.setup_logger('Login', ReadConfig.get_logs_directory() + "/Test_login.log",
                                       level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_application(self):
        self.get_url(ReadConfig.get_application_url())
        time.sleep(5)

    def open_login_page(self):
        self.driver.find_element(By.NAME, self.username).send_keys(ReadConfig.getUserID())
        print(ReadConfig.getUserID)
        time.sleep(3)
        self.driver.find_element(By.NAME, self.password).send_keys(ReadConfig.getPassword())
        time.sleep(3)
        self.click(self.submit)

    def logout_button(self):
        self.click(self.dropdown)
        self.click(self.logout)

    def open_logipage_xl(self):
        time.sleep(5)
        rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in an excel:", rows)
        lst_status = []
        for r in range(2, rows + 1):
            user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            print(user)
            password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            print(password)
            exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            print(exp)

            self.driver.find_element(By.NAME, self.username).send_keys(user)
            time.sleep(3)
            self.driver.find_element(By.NAME, self.password).send_keys(password)
            time.sleep(3)
            self.click(self.submit)
            time.sleep(4)
            if "dashboard" in self.driver.current_url:
                if exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.logout_button()
                    time.sleep(3)
                    lst_status.append("Pass")
                elif exp == 'Fail':
                    self.logger.info("**** failed ****")
                    self.logout_button()
                    lst_status.append("Fail")
            elif "dashboard" not in self.driver.current_url:
                if exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
            time.sleep(5)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            print("DDT Login test passed")
        else:
            self.logger.error("******* DDT Login test failed **********")
            assert False
