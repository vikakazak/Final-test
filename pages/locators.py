from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "div.login_form")
    register_form = (By.CSS_SELECTOR, "div.register_form")

class ProductPageLocators():
    add_to_basket_button = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group>a")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE=(By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS=(By.CSS_SELECTOR, "#basket_formset")
