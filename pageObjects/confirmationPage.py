from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    countryConfirmed = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitBtn = (By.CSS_SELECTOR, "[type='submit']")
    successText = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)
        # driver.find_element_by_id("country")
        # * is necessary since the object (country) is a tupple

    def getCountryConfirmed(self):
        return self.driver.find_element(*ConfirmPage.countryConfirmed)
        # driver.find_element_by_link_text("India")
        # * is necessary since the object (countryConfirmed) is a tupple

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)
        # driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
        # * is necessary since the object (checkBox) is a tupple

    def getSubmitBtn(self):
        return self.driver.find_element(*ConfirmPage.submitBtn)
        # driver.find_element_by_css_selector("[type='submit']")
        # * is necessary since the object (submitBtn) is a tupple

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.successText)
        # driver.find_element_by_css_selector("[class*='alert-success']")
        # * is necessary since the object (successText) is a tupple