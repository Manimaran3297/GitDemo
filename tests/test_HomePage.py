import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        log.info("firstname is entered")
        # driver.find_element_by_name("name").send_keys("Ticvic")
        time.sleep(5)
        homepage.getEmail().send_keys(getData["lastname"])
        log.info("lastname is entered")
        #driver.find_element_by_name("email").send_keys("test@gmail.com")
        time.sleep(3)
        #driver.find_element_by_id("exampleInputPassword1").send_keys("Password")
        homepage.getCheckBox().click()
        #it is reusable and define it in baseclass
         #sel = Select(homepage.getGender())
         #sel.select_by_visible_text("Male")

        self.selectOptionByText(homepage.getGender(), getData["gender"])
        log.critical("gender is selected")
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text
        #for refreshing and passing datas like data provider we use this.
        self.driver.refresh()

        assert ("Success" in alertText)
        #dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        #dropdown.select_by_visible_text("Female")
        #time.sleep(5)
        #dropdown.select_by_index(0)
        #time.sleep(5)

            #driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/input").click()
            #time.sleep(3)
            #message = driver.find_element_by_class_name("alert-success").text
            #print(message)

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self,request):
        return request.param