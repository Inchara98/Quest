import time

from selenium.webdriver.common.by import By

from Utilities.readProperties import ReadConfig

from pandas import read_csv


class Test_002_DDT_Login:
    baseUrl = "https://opensource-demo.orangehrmlive.com/"
    path = "/home/inchara/PycharmProjects/Quest/TestData/credentials.csv"

    def test_login_ddt(self, setup):
        # self.logger.info("***********************Test_002_Login_ddt*****************************")
        # self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)
        path = "/home/inchara/PycharmProjects/Quest/TestData/credentials.csv"
        data = read_csv(path)
        username = data['Username'].to_list()
        password = data['Password'].to_list()

        i = 0

        for i in range(len(data)):
            time.sleep(3)
            self.driver.find_element(By.NAME, "username").send_keys(username[i])
            self.driver.find_element(By.NAME, "password").send_keys(password[i])
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(5)
            self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown").click()
            self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]").click()

            # self.driver.find_element_by_id("username").clear()
            # self.driver.find_element_by_name("password").clear()

            # error_message = self.driver.find_element_by_tag_name("p").get_attribute('value')
            # print(error_message)

    # def test_login2_page_tittle(self, setup):
    #     self.logger.info("***********************Test_001_Login*****************************")
    #     self.logger.info("********************test_login_page_tittle started*********************")
    #     self.driver = setup
    #     self.loginpage = Login(self.driver)
    #     self.loginpage.open_application()
    #
    #     time.sleep(5)
    #     self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
    #     print("Number of rows in an excel:", self.rows)
    #     lst_status = []
    #
    #     for r in range(2, self.rows + 1):
    #         self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
    #         print(self.user)
    #         self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
    #         print(self.password)
    #         self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
    #         print(self.exp)
    #
    #         self.driver.find_element(By.NAME, "username").send_keys(self.user)
    #         time.sleep(3)
    #         self.driver.find_element(By.NAME, "password").send_keys(self.password)
    #         time.sleep(3)
    #         self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #         time.sleep(4)
    #         if "dashboard" in self.driver.current_url:
    #             if self.exp == 'Pass':
    #                 self.logger.info("**** passed ****")
    #                 self.loginpage.logout_button()
    #                 time.sleep(3)
    #                 lst_status.append("Pass")
    #             elif self.exp == 'Fail':
    #                 self.logger.info("**** failed ****")
    #                 self.loginpage.logout_button()
    #                 lst_status.append("Fail")
    #         elif "dashboard" not in self.driver.current_url:
    #             if self.exp == 'Pass':
    #                 self.logger.info("**** failed ****")
    #                 lst_status.append("Fail")
    #             elif self.exp == 'Fail':
    #                 self.logger.info("**** passed ****")
    #                 lst_status.append("Pass")
    #         print(lst_status)
    #         time.sleep(5)
    #     if "Fail" not in lst_status:
    #         self.logger.info("******* DDT Login test passed **********")
    #         assert True
    #     else:
    #         self.logger.error("******* DDT Login test failed **********")
    #         assert False