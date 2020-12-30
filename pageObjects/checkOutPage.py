from selenium.webdriver.common.by import By
from pageObjects.confirmationPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)
        # driver.find_elements_by_css_selector(".card-title a")
        # * is necessary since the object (cardTitle) is a tupple

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)
        # driver.find_elements_by_css_selector(".card-footer button")
        # * is necessary since the object (cardFooter) is a tupple

    def getCheckOutBtn(self):
        return self.driver.find_element(*CheckOutPage.checkOutBtn)
        # driver.find_element_by_css_selector("a[class*='btn-primary']")
        # * is necessary since the object (checkOutBtn) is a tupple

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        # driver.find_element_by_xpath("//button[@class='btn btn-success']")
        # * is necessary since the object (checkOut) is a tupple

        confirmPage = ConfirmPage(self.driver)
        return confirmPage

    # Be aware of the singular or plural element when use .find_element/s
    # It will affect whether we can click an element or not