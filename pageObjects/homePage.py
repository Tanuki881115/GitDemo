from selenium.webdriver.common.by import By
from pageObjects.checkOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkBoxBtn = (By.ID, "exampleCheck1")
    genderSel = (By.ID, "exampleFormControlSelect1")
    submitBtn = (By.CSS_SELECTOR, "input[class*='btn-success']")
    alertText = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        # driver.find_element_by_css_selector("a[href*='shop']")
        # * is necessary since the object (shop) is a tuple

        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)
        # driver.find_element_by_css_selector("[name='name']")

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
        # driver.find_element_by_name("email")

    def getCheckBoxBtn(self):
        return self.driver.find_element(*HomePage.checkBoxBtn)
        # driver.find_element_by_id("exampleCheck1").

    def getGenderSel(self):
        return self.driver.find_element(*HomePage.genderSel)
        # driver.find_element_by_id("exampleFormControlSelect1")

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submitBtn)
        # driver.find_element_by_xpath("//input[@value='Submit']")

    def getAlertText(self):
        return self.driver.find_element(*HomePage.alertText)
        # driver.find_element_by_css_selector("[class*='alert-success']")
