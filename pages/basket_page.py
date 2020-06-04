from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        empty_basket=self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        empty_basket_text=empty_basket.text
        assert empty_basket_text=="Your basket is empty. Continue shopping", \
            "Basket is not empty, but it should be"
    def basket_should_not_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket has items"