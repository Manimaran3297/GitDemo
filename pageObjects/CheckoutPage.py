from selenium.webdriver.common.by import By


class ChekOutPage:

    def __init__(self,driver):
        self.driver = driver

    #driver.find_elements_by_css_selector(".card-title a")
    #self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

    cardTitle = (By.CSS_SELECTOR,".card-title a")
    cardFooter = (By.CSS_SELECTOR,".card-footer button")
    checkOut =  (By.CSS_SELECTOR,"a[class*='btn-primary")
    checkOuttocart = (By.XPATH,"//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*ChekOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*ChekOutPage.cardFooter)

    def checkOutbutton(self):
        return self.driver.find_element(*ChekOutPage.checkOut)
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

    def CheckoutCart(self):
        return self.driver.find_element(*ChekOutPage.checkOuttocart)