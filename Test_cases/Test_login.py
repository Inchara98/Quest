from Utilities.readProperties import ReadConfig
from Logs.Log import log_details
from pandas import read_csv


class Test_002_DDT_Login:
    baseUrl = "https://opensource-demo.orangehrmlive.com/"
    path = "/home/inchara/PycharmProjects/PDS/TestData/credentials.csv"

    logger = log_details.logen()

    def test_login_ddt(self, setup):
        self.logger.info("***********************Test_002_Login_ddt*****************************")
        self.logger.info("********************verifying Login Test********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)

        path = "/home/inchara/PycharmProjects/Quest/TestData/credentials.csv"
        data = read_csv(path)
        username = data['Username'].to_list()
        password = data['Password'].to_list()

        i = 0

        for i in range(len(data)):
            self.driver.find_element_by_id("username").send_keys(username[i])
            self.driver.find_element_by_name("password").send_keys(password[i])
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
            self.driver.find_element_by_id("username").clear()
            self.driver.find_element_by_name("password").clear()

            # error_message = self.driver.find_element_by_tag_name("p").get_attribute('value')
            # print(error_message)
