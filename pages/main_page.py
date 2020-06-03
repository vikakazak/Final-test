from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

# class MainPage(BasePage):
    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     login_link.click()
    #     #return LoginPage(browser=self.browser, url=self.browser.current_url)
    #     #alert = self.browser.switch_to.alert
    #     #alert.accept()
    #
    # def should_be_login_link(self):
class MainPage(BasePage):   #заглушка
    pass