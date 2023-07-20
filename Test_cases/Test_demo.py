import logging
import time

from PageObjects.login import Login
from Utilities import CustomLogger
from Utilities.readProperties import ReadConfig


class Testlogin:
    loginpage = None

    print("*********8**"+ReadConfig.get_logs_directory())
    # logger = CustomLogger.setup_logger('Login', ReadConfig.get_logs_directory() + "/Test_login.log",
    #                                    level=logging.DEBUG)


    def test_login_page_tittle(self, setup):
        pass
        # self.logger.info("***********************Test_001_Login*****************************")
        # self.logger.info("********************test_login_page_tittle started*********************")
        # self.driver = setup
        # self.loginpage = Login(self.driver)
        # self.loginpage.open_application()
        # time.sleep(5)
        # self.loginpage.open_login_page()
        # time.sleep(3)
        # if "dashboard" in self.driver.current_url:
        #     self.driver.close()
        #     self.logger.info("******************** test_login_page_tittle test case passed ************************")
        # else:
        #     self.driver.get_screenshot_as_file(ReadConfig.get_ss_path() + "test_login_page_tittle.png")
        #     self.driver.close()
        #     self.logger.error("******************** test_login_page_tittle test case failed **************************")
        #     assert False
        # self.logger.info("******************** test_login_page_tittle ended ************************")
