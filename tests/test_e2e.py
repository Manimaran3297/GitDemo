import pytest
from selenium import webdriver
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import ChekOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass





class TestOne(BaseClass):

     def test_e2e(self):

         log = self.getLogger()
         homePage = HomePage(self.driver)
         checkoutpage = homePage.shopItems()
         log.info(("getting all card titles"))
          #self.driver.find_element_by_css_selector("a[href*='shop']").click()
          #checkOutPage = ChekOutPage(self.driver)
           #cards = self.driver.find_elements_by_css_selector(".card-title a")
         cards = checkoutpage.getCardTitles()
         time.sleep(5)
         i = -1
         for card in cards:
             i = i + 1
             cardText = card.text
             print(cardText)
             if cardText == "Blackberry":
                 checkoutpage.getCardFooter()[i].click()
                 log.info("click on blackberry")
         checkoutpage.checkOutbutton().click()
         log.error("blackberry not selected")
         checkoutpage.CheckoutCart().click()
         self.driver.find_element_by_id("country").send_keys("ind")
         log.info("searching for india")
         time.sleep(5)
         self.verifyLinkPresence("India")
         log.critical("network is slow")
         #element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"India")))
         self.driver.find_element_by_link_text("India").click()
         self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
         self.driver.find_element_by_css_selector("[type='submit']").click()
         log.warning("payment may not succeed")
         textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
         log.info("message received is"+ textMatch)
         assert ("Success! Thank you! so much" in textMatch)

