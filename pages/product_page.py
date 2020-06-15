from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_message_about_adding(self):
        name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_BASKET)
        name_in_basket_text = name_in_basket.text
        name_on_product_page = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_ON_PRODUCT_PAGE)
        name_on_product_page_text = name_on_product_page.text
        assert name_in_basket_text == name_on_product_page_text, "Name of book should be the same"

    def should_be_message_basket_total(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_IN_BASKET)
        price_in_basket_text = price_in_basket.text
        price_on_product_page = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_ON_PRODUCT_PAGE)
        price_on_product_page_text = price_on_product_page.text
        assert price_in_basket_text == price_on_product_page_text, "Price of book should be the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but it should"

