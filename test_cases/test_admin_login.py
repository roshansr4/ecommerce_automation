import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config #imported read config class from utilities package's read_property file
from utilities.custom_logger import Log_maker

class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()                                         #"https://admin-demo.nopcommerce.com/login" - replaced
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_maker.log_gen() #returns logger from log_gen()


    @pytest.mark.regression
    def test_title_verification(self, setup): #test to verify the title
        self.logger.info("***********Test_01_Admin_Login***********")
        self.logger.info("***********verification of admin page title***********")
        # Note: Why logs? to improve debugging, track test execution,
        # and understand application behavior, especially when failures occur,
        # by providing a detailed trail of events. Stored in nopcommerce.log.
        #Created a utilities file custom_logger.py first and added a static method
        #under class Log_maker and imported Log_maker
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"

        if act_title == exp_title:
            self.logger.info("***********test title verification title matched***********") #Adding logs
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("***********test title verification title NOT matched***********")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self, setup):
        self.logger.info("***********test_valid_admin_login started***********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class= 'content-header']/h1" ).text
        if act_dashboard_text == "Dashboard":
            self.logger.info("***********Dashboard text found***********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\valid_admin_login.png")
            self.driver.close()
            assert False


    def test_invalid_admin_login(self, setup):
        self.logger.info("***********test_invalid_admin_login started***********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)       #creating the object and passing the driver
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH, '//li').text
        if error_message == 'No customer account found':
            self.logger.info("***********test_invalid_admin_login error message matched***********")

            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")
            self.driver.close()
            assert False





